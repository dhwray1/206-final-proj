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
    ingredient_dict = {}
    param = {"i": ingredient}
    response = requests.get(url, params=param)
    #print(response.text)
    x=json.loads(response.text)
    for key in x:
        for dict in x[key]:
            #print(dict)
            name = dict['strMeal']
            id = dict['idMeal']
            ingredient_dict[ingredient] =  [name, id]
            #print(db_list)
            print(ingredient_dict)
            db_list.append(ingredient_dict)
    #print(x)
print(db_list)

def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn

def create_meal_table(cur, conn):
    # cur.execute('DROP TABLE IF EXISTS Chicken')
    cur.execute('CREATE TABLE IF NOT EXISTS "Meals"("id" INTEGER PRIMARY KEY, "Ingredient" TEXT, "strMeal" TEXT)')
    for number in range(100):
        id = number
        # cur.execute('SELECT MAX id')
        # if returned value == none
        # count = 0
        # for smtg in range(count, count+25):
        # insert id 
        conn.commit()

# def create_eggs_table(cur, conn):
#     # cur.execute('DROP TABLE IF EXISTS Eggs')
#     cur.execute('CREATE TABLE IF NOT EXISTS "Meals with Eggs"("idMeal" INTEGER PRIMARY KEY, "strMeal" TEXT)')
#     conn.commit()

# def create_sugar_table(cur, conn):
#     # cur.execute('DROP TABLE IF EXISTS Sugar')
#     cur.execute('CREATE TABLE IF NOT EXISTS "Meals with Sugar"("idMeal" INTEGER PRIMARY KEY, "strMeal" TEXT)')
#     conn.commit()




def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('meals.db')
    create_meal_table(cur, conn)
    # create_eggs_table(cur, conn)
    # create_sugar_table(cur, conn)

main()