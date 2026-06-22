from Json.jsonFunctions import *
import Save_Entry.saveEntry as s 

PATH = s.JSON_PATH
def searchEntry():
    search = input("Enter a site to search: ")
    match = False

    data = loadJson(PATH)

    for entry in data:
        if search.lower() in entry["Site"].lower():
            match = True
            print(f"{entry["Username"]} | {entry["Site"]} | {entry["Password"]}")
            
    if not match:
        print(f"Cant Found {search}.....")