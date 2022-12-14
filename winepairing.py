import requests
import json
import unittest
import sqlite3
import os

#
# Your name: Vikram Reddy
# Who you worked with: Dhwani R, Anjali Francis 
#


API_KEY = "363378b0a69f4f7d8ef8c3d8022b572b"



wine_list = ["tannat", "white_wine", "dry_white_wine", "assyrtiko", "pinot_blanc", "cortese", "roussanne", "moschofilero", 
"muscadet", "viognier", "verdicchio", "greco", "marsanne", "white_burgundy", "chardonnay", "gruener_veltliner", "white_rioja", "frascati",
"gavi", "l_acadie_blanc", "trebbiano", "sauvignon_blanc", "catarratto", "albarino", "arneis", "verdejo", "vermentino", "soave", "pinot_grigio",
"dry_riesling", "torrontes", "mueller_thurgau", "grechetto", "gewurztraminer", "chenin_blanc", "white_bordeaux", "semillon", "riesling",
"sauternes", "sylvaner", "lillet_blanc", "red_wine", "dry_red_wine", "petite_sirah", "zweigelt", "baco_noir", "bonarda", "cabernet_franc", 
"bairrada", "barbera_wine", "primitivo", "pinot_noir", "nebbiolo", "dolcetto", "tannat", "negroamaro", "red_burgundy", "corvina", "rioja",
"cotes_du_rhone", "grenache", "malbec", "zinfandel", "sangiovese", "carignan", "carmenere", "cesanese", "cabernet_sauvignon", "aglianico",
"tempranillo", "shiraz", "mourvedre", "merlot", "nero_d_avola", "bordeaux", "marsala", "port", "gamay", "dornfelder", "concord_wine", "sparkling_red_wine", 
"pinotage", "agiorgitiko", "dessert_wine", "pedro_ximenez", "moscato", "late_harvest", "ice_wine", "white_port", "lambrusco_dolce", "madeira", "banyuls", 
"vin_santo", "port", "rose_wine", "sparkling_rose", "sparkling_wine", "cava", "cremant", "champagne", "prosecco", "spumante", 
"sparkling_rose", "sherry", "cream_sherry", "dry_sherry", "vermouth", "dry_vermouth", "fruit_wine", "mead"]

# print(len(wine_list))

base_url = "https://api.spoonacular.com/food/wine/dishes"
lst=[]
for wine in wine_list:
    param_dict = {'wine': wine, 'apiKey': API_KEY }
    r = requests.get(base_url, params = param_dict)
    #print(r)
    data = r.text
    x = json.loads(data) #dictionary
    #print(dict_list)
#     wine_dict={}
#     # print(data)
#     final_list.append(dict_list)
    # print(x)
   

    wine_dict = {}
    if x.get("status"):
        if x["status"]=="failure":
            wine_dict[wine]="0"
    else:
        wine_dict[wine]=x["pairings"]
# print(wine_dict)
    lst.append(wine_dict)
# print(lst)

winedb_lst = []
for i in range(len(lst)): 
    my_new_string = str(lst[i].keys())
    my_new_string = my_new_string.strip("dict_keys(")
    my_new_string = my_new_string.strip("['")
    my_new_string = my_new_string.rstrip("'])")
    winedb_lst.append(my_new_string)


def setUpDatabase(db_name):
    path = os.path.dirname(os.path.abspath(__file__))
    conn = sqlite3.connect(path+'/'+db_name)
    cur = conn.cursor()
    return cur, conn



def create_wine_table(cur, conn):
    cur.execute('CREATE TABLE IF NOT EXISTS "Wines"("id" INTEGER PRIMARY KEY,"Wine" TEXT)')
    cur.execute('CREATE TABLE IF NOT EXISTS "Serving"("id" INTEGER PRIMARY KEY,"Wine_id" INTEGER, "Meal" TEXT)')

    cur.execute("SELECT count(*) FROM Wines")
    count = cur.fetchone()[0]
    num_count = 0


    cur.execute("SELECT count(*) FROM Serving")
    serving_id = cur.fetchone()[0]

    while count < len(winedb_lst) and num_count < 25:
        cur.execute("INSERT INTO Wines (id, Wine) VALUES (?,?)", (count+1, winedb_lst[count]))
        for meal in lst[count][winedb_lst[count]]:
            if meal == '0':
                break
            cur.execute("INSERT INTO Serving (id, Wine_id, Meal) VALUES (?,?,?)", (serving_id+1, count+1, meal))
            serving_id += 1
        num_count += 1
        count += 1
        
    conn.commit()

def calculate_data(cur, conn):
    cur.execute("SELECT s.MEAL FROM Serving s JOIN WINES w ON w.id = s.Wine_id WHERE w.Wine = 'white_wine'")
    (cur.execute("Select count(*) FROM Serving"))
    total_wine_number=(cur.fetchone())
    # print(total_wine_number)
    (cur. execute("SELECT count(s.id) FROM Serving s JOIN Wines w on s.Wine_id= w.id WHERE w.Wine='white_wine'" ))
    white_wine_number=(cur.fetchone())
    frequency= (white_wine_number[0]/total_wine_number[0])*100
    file=open("my_file.txt", "a")
    file.write("The meals that are best paired with white wines which was found using join tables are pho, fish, crab, stew, and carp." + "\n"
    "White whine pairings consists of " + str(round(frequency,2)) + " percentage of all wine and meal pairings in the database." + "\n")
    file.close()




# def calculations(cur, conn):

def main():
    # SETUP DATABASE AND TABLE
    cur, conn = setUpDatabase('meals.db')
    #create_db_list()
    create_wine_table(cur, conn)
    calculate_data(cur, conn)
    # create_eggs_table(cur, conn)
    # create_sugar_table(cur, conn)

main()










