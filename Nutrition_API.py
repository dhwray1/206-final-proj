import requests
import json
lst=["butter" , "chicken", "eggs", "sugar", "salt", "bok choy", "drumstick", "tomato", "lemon", "potato",
 "spinach", "onion", "mushroom", "radish", "chives", "coriander", "paprika", "red chili", "saffron", "beef", "turkey", "salmon",
  "pork", "ham","crab", "parmesan cheese", "cheddar cheese", "yogurt", "kiwi", "blueberry", "strawberry", "mango", "watermelon", 
  "papaya", "orange","olive", "pear", "shrimp", "tuna", "hazelnut", "pine nuts", "pistachio","almonds", "walnut",
   "vinegar", "white wine", "Red wine", "yeast", "white pepper", "chocolate", "quinoa","lettuce", "leek", "pumpkin", "yam", "jalapeno",
    "jackfruit", "beans", "garlic", "pickle", "cucumber", "zucchini", "corn", "celery", "carrot", "cauliflower", "capsicum", "broccoli",
     "beetroot","cabbage", "bacon", "grapefruit", "coconut", "cherry",
 "banana", "kale", "cilantro", "parsnips","peas","tofu","parsley","thyme","basil",
 "peanut","turmeric","dill","fennel","cod","ginger","squid","lobster","nutmeg","cardamom","cloves","cinnamon","cayenne","avocado", "chickpeas", "barley", "mussel"]

# print(len(lst))


url= "https://api.edamam.com/api/nutrition-data"
for item in lst:
    param= {"app_id":"c100b32f", "app_key":"dfea42f04a0fa63a54f6ca87b260fe97", "ingr":item, "nutrition-type": "logging"}
    response= requests.get(url, params= param)
    # print(response.text)
    x=json.loads(response.text) #Dictionary
# print(x)
    # index json to create my own dic
    # index dic to put into SQL Database outside for loop
    nutrient_dict = {}
    #ALl in grams
    calories = x['calories']
    fat= round(x["totalNutrients"]["FAT"]["quantity"],2)
    protein= round(x["totalNutrients"]["PROCNT"]["quantity"],2)
    carbohydrates=round(x[ "totalNutrients"]["CHOCDF"]["quantity"] ,2)
    nutrient_dict[item]= [calories, fat, protein, carbohydrates] #SHOULD THIS BE IN DICT FORMAT, HOW SHOULD IT LOOK TO PUT INTO THE DATABSE TABLE?
    # print(nutrient_dict)
    


           

#Part 3
#select into all databases to get some numbers and perform calc
#Doesn't have to be one big seelct statmenet. differnt statements to access different data from each tables.





