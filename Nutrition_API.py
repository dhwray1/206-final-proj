import requests
import json
import unittest
import sqlite3
import os

lst=["butter" , "chicken", "eggs", "sugar", "salt", "bok choy", "drumstick", "tomato", "lemon", "potato",
 "spinach", "onion", "mushroom", "radish", "chives", "coriander", "paprika", "red chili", "saffron", "beef", "turkey", "salmon",
  "pork", "ham","crab", "parmesan cheese", "cheddar cheese", "yogurt", "kiwi", "blueberry", "strawberry", "mango", "watermelon", 
  "papaya", "orange","olive", "pear", "shrimp", "tuna", "hazelnut", "pine nuts", "pistachio","almonds", "walnut",
   "vinegar", "white wine", "Red wine", "yeast", "white pepper", "chocolate", "quinoa","lettuce", "leek", "pumpkin", "yam", "jalapeno",
    "jackfruit", "beans", "garlic", "pickle", "cucumber", "zucchini", "corn", "celery", "carrot", "cauliflower", "capsicum", "broccoli",
     "beetroot","cabbage", "bacon", "grapefruit", "coconut", "cherry",
 "banana", "kale", "cilantro", "parsnips","peas","tofu","parsley","thyme","basil",
 "peanut","turmeric","dill","fennel","cod","ginger","squid","lobster","nutmeg","cardamom","cloves","cinnamon","cayenne","avocado", "chickpeas",
  "barley", "mussel"]

# print(len(lst))


url= "https://api.edamam.com/api/nutrition-data"
final_lst=[]
# for item in lst:
#     param= {"app_id":"3b2f2a33", "app_key":"125bbe77c7affc11fa2e9496a74b6395", "ingr":item, "nutrition-type": "logging"}
#     response= requests.get(url, params= param)
#     x=json.loads(response.text) #Dictionary

#     nutrient_dict = {}
   
#     #ALl in grams
#     calories = x['calories']
#     fat= round(x["totalNutrients"]["FAT"]["quantity"],2)
#     protein= round(x["totalNutrients"]["PROCNT"]["quantity"],2)
#     carbohydrates=round(x[ "totalNutrients"]["CHOCDF"]["quantity"] ,2)
#     nutrient_dict[item]= [calories, fat, protein, carbohydrates] #SHOULD THIS BE IN DICT FORMAT, HOW SHOULD IT LOOK TO PUT INTO THE DATABSE TABLE?
#     final_lst.append(nutrient_dict)
# # print(final_lst)
    
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
    
def create_calories_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS "Calories"("id" INTEGER PRIMARY KEY,"Ingredient" TEXT, "Calories" TEXT)')
    for number in range(100):
        id = number
    conn.commit()


def create_nutritionval_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS "Nurtrional Value"("id" INTEGER PRIMARY KEY, "Ingredient" TEXT, "Fat" TEXT, "Protein" TEXT, "Carbohydrates" TEXT)')
    for number in range(100):
       id = number
    conn.commit()

#One table is ingredient(primary key) with calories
#Second table is Nutritional value of ingredients (primary key) (Fat, protein, carbs)


def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('meals.db')
    create_calories_table(cur, conn)
    create_nutritionval_table(cur, conn)


main()

           
#Part 3
#select into all databases to get some numbers and perform calc
#Doesn't have to be one big seelct statmenet. differnt statements to access different data from each tables.





