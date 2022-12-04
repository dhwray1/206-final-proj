import requests
import json
lst=["butter" , "chicken", "eggs", "sugar", "salt", "bok choy", "drumstick", "tomato", "lemon", "potato",
 "spinach", "onion", "mushroom", "radish", "chives", "coriander", "paprika", "red chilli", "saffron", "beef", "turkey", "salmon",
  "pork", "ham","crab", "parmesan cheese", "cheddar cheese", "yogurt", "kiwi", "blueberry", "strawberry", "mango", "watermelon", 
  "papaya", "orange","olive", "pear", "lychee", "shrimp", "tuna", "hazelnut", "pine nuts", "pistachio","almonds", "walnut",
   "vinegar", "white wine", "Red wine", "yeast", "white pepper", "chocolate", "quinoa","lettuce", "leek", "pumpkin", "yam", "jalapeno",
    "jackfruit", "beans", "garlic", "pickle", "cucumber", "zucchini", "corn", "celery", "carrot", "cauliflower", "capsicum", "broccoli",
     "beetroot","cabbage", "mutton", "bacon", "grapefruit", "coconut", "cherry",
 "banana", "kale", "cilantro", "parsnips","peas","tofu","parsley","thyme","basil",
 "peanut","turmeric","dill","fennel","cod","ginger",
 "sardine","squid","lobster","nutmeg","cardamom","cloves","cinnamon","cayenne","avacado"]

# print(len(lst))

url= "https://api.edamam.com/api/nutrition-data"
for item in lst:
    param= {"app_id":"c100b32f", "app_key":"dfea42f04a0fa63a54f6ca87b260fe97", "ingr":item}
    response= requests.get(url, params= param)
    # print(response.text)
    x=json.loads(response.text)
    #index json to create my own dic
    #index dic to put into SQL Database outside for loop
    print(x)


#Part 3
#select into all databases to get some numbers and perform calc
#Doesn't have to be one big seelct statmenet. differnt statements to access different data from each tables.





