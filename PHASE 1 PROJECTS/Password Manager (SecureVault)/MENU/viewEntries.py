from Json.jsonFunctions import *
import Save_Entry.saveEntry as s 


PATH = s.JSON_PATH
print(PATH)

def viewEntries():
    entries = loadJson(PATH)

    for i, entry in enumerate(entries, start=1):
            print(f"{i}. {entry["Username"]} | {entry["Site"]} | {entry["Password"]}")