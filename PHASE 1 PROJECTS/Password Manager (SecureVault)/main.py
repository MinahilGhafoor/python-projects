import Password_Management.masterPassword as mp
import MENU.addEntry as aE
import MENU.viewEntries as vE
import MENU.searchEntry as sE
import MENU.delEntry as dE
import MENU.quitProgram as qP
import os
import time

#############################################################################################
def welcome():
    print("============================")
    print("     🔐 SecureVault")
    print("============================")

def cls():
     return os.system('cls') if os.name == "nt" else "clear"
##############################################################################################
  

MAIN_MENU = {"Add Entry" : aE.addEntry, 
             "ViewAll" : vE.viewEntries, 
             "Search" : sE.searchEntry,
             "Delete Entry" : dE.delEntry,
             "Exit" : qP.quito}
def menu():  
     while True: 
          time.sleep(10)
          cls()
          print(f"============================\nMAIN MENU\n============================")

          for (idx, opt) in enumerate(MAIN_MENU, start=1):
               print(f"{idx}. {opt}")

          print("============================")

          choice = input("Choice: ") 

          try:    
               list(MAIN_MENU.values())[int(choice) - 1]()
          except:
               continue


def main():
     welcome()
     if mp.authorize():
          menu()
    
if __name__ == "__main__":
     main()