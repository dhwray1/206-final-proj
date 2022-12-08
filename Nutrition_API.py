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
for item in lst:
    param= {"app_id":"3b2f2a33", "app_key":"125bbe77c7affc11fa2e9496a74b6395", "ingr":item, "nutrition-type": "logging"}
    response= requests.get(url, params= param)
    x=json.loads(response.text) #Dictionary

    nutrient_dict = {}
   
    #ALl in grams
    # calories = x['calories']
    fat= round(x["totalNutrients"]["FAT"]["quantity"],2)
    protein= round(x["totalNutrients"]["PROCNT"]["quantity"],2)
    carbohydrates=round(x[ "totalNutrients"]["CHOCDF"]["quantity"] ,2)
    nutrient_dict[item]= [fat, protein, carbohydrates] #SHOULD THIS BE IN DICT FORMAT, HOW SHOULD IT LOOK TO PUT INTO THE DATABSE TABLE?
    final_lst.append(nutrient_dict)
# print(final_lst)


db_lst = []
for i in range(len(final_lst)): 
    my_new_string = str(final_lst[i].keys())
    my_new_string = my_new_string.strip("dict_keys(")
    my_new_string = my_new_string.strip("['")
    my_new_string = my_new_string.rstrip("'])")
    db_lst.append(my_new_string)
# print(db_lst)
    
def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn
    
def create_fat_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS "Fat"("id" INTEGER PRIMARY KEY,"Ingredient" TEXT, "Fat" TEXT)')
    cur.execute("SELECT count(*) FROM Fat")
    count = cur.fetchone()[0]
    num_count = 0
    while count < len(db_lst) and num_count < 25:
        cur.execute("INSERT INTO Fat (id, Ingredient, Fat) VALUES (?,?,?)", (count+1, db_lst[count], final_lst[count][db_lst[count]][0]))
        num_count += 1
        count += 1
    conn.commit()

def create_protein_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS "Protein"("id" INTEGER PRIMARY KEY,"Ingredient" TEXT, "Protein" TEXT)')
    cur.execute("SELECT count(*) FROM Protein")
    count = cur.fetchone()[0]
    num_count = 0
    while count < len(db_lst) and num_count < 25:
        cur.execute("INSERT INTO Protein (id, Ingredient, Protein) VALUES (?,?,?)", (count+1, db_lst[count], final_lst[count][db_lst[count]][1]))
        num_count += 1
        count += 1
    conn.commit()    
    

def create_carb_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS "Carbohydrates"("id" INTEGER PRIMARY KEY, "Ingredient" TEXT, "Carbohydrates" TEXT)')
    cur.execute("SELECT count(*) FROM Carbohydrates")
    count = cur.fetchone()[0]
    num_count = 0
    while count < len(db_lst) and num_count < 25:
        cur.execute("INSERT INTO Carbohydrates (id, Ingredient, Carbohydrates) VALUES (?,?,?)", (count+1, db_lst[count], final_lst[count][db_lst[count]][2]))
        num_count += 1
        count += 1
    conn.commit()



def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('meals.db')
    create_fat_table(cur, conn)
    create_protein_table(cur, conn)
    create_carb_table(cur, conn)


main()

           
#Part 3
#select into all databases to get some numbers and perform calc
#Doesn't have to be one big seelct statmenet. differnt statements to access different data from each tables.





