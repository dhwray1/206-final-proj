import requests
import json
import unittest
import sqlite3
import os
import re
import matplotlib.pyplot as plt

API_KEY = '1'
url = "https://www.themealdb.com/api/json/v1/1/filter.php?"
ingredient_list = ["chicken breast", "eggs", "sugar"]

db_list = []
for ingredient in ingredient_list:
    param = {"i": ingredient}
    response = requests.get(url, params=param)
    #print(response.text)
    x=json.loads(response.text)
    for key in x:
        for dict in x[key]:
            ingredient_dict = {}
            #print(dict)
            name = dict['strMeal']
            id = dict['idMeal']
            ingredient_dict[ingredient] =  [name, id]
            #print(db_list)
            #print(ingredient_dict)
            db_list.append(ingredient_dict)
    #print(x)
#print(db_list)
long_ing_list = []
for i in range(len(db_list)): 
    my_new_string = str(db_list[i].keys())
    my_new_string = my_new_string.strip("dict_keys(")
    my_new_string = my_new_string.strip("['")
    my_new_string = my_new_string.rstrip("'])")
    long_ing_list.append(my_new_string)
#print(long_ing_list)

    # final_db_dict = {}
    # for i in range(len(db_list)):
    #     final_db_dict[i] = db_list[i]
    # print(final_db_dict)

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_meal_table(cur, conn):
    # cur.execute('DROP TABLE IF EXISTS Chicken')
    cur.execute('CREATE TABLE IF NOT EXISTS "Meals"("id" INTEGER PRIMARY KEY, "Ingredient" TEXT, "strMeal" TEXT, "MealID" INTEGER)')
    # for number in range(100):
    #     id = number
    # count = 0
    cur.execute("SELECT count(*) FROM Meals")
    count = cur.fetchone()[0]
        #for lst in dog_lst:
            #for tup in lst:
                #print(tup[0])
                #cur.execute("INSERT INTO Dogs (breed, life_span, weight, height) VALUES (?,?,?,?)", (tup[0], tup[1], tup[2], tup[3]))
                #count+=1
        #cur.execute('SELECT MAX id')
    num_count = 0
    while count < len(long_ing_list) and num_count < 25:
    # for index in range(len(long_ing_list)):
        cur.execute("INSERT INTO Meals (id, Ingredient, strMeal, MealID) VALUES (?,?,?,?)", (count+1, long_ing_list[count], db_list[count][long_ing_list[count]][0], db_list[count][long_ing_list[count]][1]))
        num_count += 1
        count += 1
         # count+=1
        # if returned value == none
        # count = 0
        # for smtg in range(count, count+25):
        # insert id 
  
    conn.commit()

    # if count == 25 or count == 50 or count == 75 or count == 100:

def calculating_data(cur, conn):
    get_meal1 = cur.execute('SELECT strMeal from Meals WHERE MealID = "53011"')
    get_meal1 = cur.fetchone()
    print(get_meal1)

    get_startingid = cur.execute("SELECT * FROM Meals WHERE MealID LIKE '53%'")
    get_startingid = cur.fetchall()
    print(len(get_startingid))

    chicken_meals = cur.execute("SELECT * FROM Meals WHERE Ingredient = 'chicken breast'")
    chicken_meals = cur.fetchall()
    print("The number of meals in our database made out of chicken is ", len(chicken_meals))
    chicken_percent = ((len(chicken_meals)/len(db_list))*100)
    print("The percentage of meals made out of chicken in our database is ", chicken_percent, "%")

    egg_meals = cur.execute("SELECT * FROM Meals WHERE Ingredient = 'eggs'")
    egg_meals = cur.fetchall()
    print("The number of meals in our database made out of eggs is ",len(egg_meals))
    egg_percent = ((len(egg_meals)/len(db_list))*100)
    print("The percentage of meals made out of eggs in our database is ", egg_percent, "%")

    sugar_meals = cur.execute("SELECT * FROM Meals WHERE Ingredient = 'sugar'")
    sugar_meals = cur.fetchall()
    print("The number of meals in our database made out of sugar is ", len(sugar_meals))
    chicken_percent = ((len(sugar_meals)/len(db_list))*100)
    print("The percentage of meals made out of chicken in our database is ", chicken_percent, "%")

def create_my_pie(): 
    labels = ['Chicken', 'Eggs', 'Sugar']
    sizes = [9, 62, 38]
    colors = ['#FFC154', '#EC6B56', '#47B39C']
    # explode = (0.1, 0, 0)

    pie = plt.pie(sizes, labels=labels, colors=colors, autopct='%1.1f%%', shadow=False, startangle=140, wedgeprops = {"edgecolor" : "black", 'linewidth': 2, 'antialiased': True})
    
    plt.axis('equal')

    hatches = ['+', '/', '.']
    # hatch_colors = ['#b57c18', '#c23b25', '#056b55']

    for i in range(len(pie[0])):
        pie[0][i].set(hatch = hatches[i], fill=True)

    plt.title("Percentage of Chicken meals, egg meals and sugar meals in our database")

    plt.show()

"""
# def create_eggs_table(cur, conn):
#     # cur.execute('DROP TABLE IF EXISTS Eggs')
#     cur.execute('CREATE TABLE IF NOT EXISTS "Meals with Eggs"("idMeal" INTEGER PRIMARY KEY, "strMeal" TEXT)')
#     conn.commit()

# def create_sugar_table(cur, conn):
#     # cur.execute('DROP TABLE IF EXISTS Sugar')
#     cur.execute('CREATE TABLE IF NOT EXISTS "Meals with Sugar"("idMeal" INTEGER PRIMARY KEY, "strMeal" TEXT)')
#     conn.commit()


#     cur.execute("CREATE TABLE IF NOT EXISTS Dogs (id INTEGER PRIMARY KEY, 'breed' TEXT, 'life_span' TEXT, 'weight' TEXT, 'height' TEXT)")
#     dog_lst=print_dog()
#     #print(dog_lst)
#     #count=1
#     for lst in dog_lst:
#         for tup in lst:
#             #print(tup[0])
#             cur.execute("INSERT INTO Dogs (breed, life_span, weight, height) VALUES (?,?,?,?)", (tup[0], tup[1], tup[2], tup[3]))
#             #count+=1
#     conn.commit()
"""

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('meals.db')
    #create_db_list()
    create_meal_table(cur, conn)
    # create_eggs_table(cur, conn)
    # create_sugar_table(cur, conn)
    calculating_data(cur, conn)
    create_my_pie()

main()