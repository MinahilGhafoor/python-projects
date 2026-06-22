import Password_Management.makePassword as mp
from Password_Management.generatePassword import *
from Site_Validation.site import *
from Save_Entry.saveEntry import *
from validInput import *
from validInput import *
##########################################################################################
def addEntry():
     SITE, USERNAME = getValidSite(), getValidInput("User name:   ")

     while (pwd := input("Generate Password (y/n): ").upper()) not in "YN": print("❌ Invalid!")

     PASSWORD = generatePassword() if pwd == "Y" else  mp.makePassword()

     print(f"✅ Entry saved for {USERNAME}@{SITE}!")
     print(PASSWORD)
     saveEntry(USERNAME, SITE, PASSWORD)
    
##########################################################################################
