import requests
import json
import unittest
import sqlite3
import os

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
print(db_list)
long_ing_list = []
for i in range(len(db_list)): 
    my_new_string = str(db_list[i].keys())
    my_new_string = my_new_string.strip("dict_keys(")
    my_new_string = my_new_string.strip("['")
    my_new_string = my_new_string.rstrip("'])")
    long_ing_list.append(my_new_string)
print(long_ing_list)

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

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('meals.db')
    #create_db_list()
    create_meal_table(cur, conn)
    # create_eggs_table(cur, conn)
    # create_sugar_table(cur, conn)

main()