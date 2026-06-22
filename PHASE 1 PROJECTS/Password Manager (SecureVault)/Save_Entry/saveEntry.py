import json
from Json.jsonFunctions import *
JSON_PATH = r"C:\Users\Acer\OneDrive\Desktop\git projects\PHASE 4 PROJECTS\Password Manager (SecureVault)\Save_Entry\savedEntries.json"



def saveEntry(user, site, password):
    data = loadJson(JSON_PATH)

    entry = {"Username" : user,
             "Site" : site,
             "Password" : password}
    
    if not entry in data:
        data.append(entry)

    writeJson(JSON_PATH, data)