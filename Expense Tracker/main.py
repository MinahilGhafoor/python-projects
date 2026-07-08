from color_ama import *
from tables import *
from menu import *
import os
#import pytts3

def cls():
    os.system('cls' if os.name == "nt" else "clear")


#************************************************************************************
def show_banner():
    print(CYAN + figlet("💰 Expense Tracker") + RESET)
    print(GREEN + "💰 Welcome to Your Expense Tracker 💰 "+ RESET)

def show_menu():
    print(YELLOW + "📋 Main Menu" + RESET)
    for i in MENU.keys():
        print(MAGENTA + i + RESET)

def main_menu():
    cls()
    while True:
        
        show_banner()
        show_menu()
        choice = menu_choice()
        list(MENU.values())[choice]()

def menu_choice():

    while True:
        choice = input(CYAN + "👉 Choose an option:  " + RESET)

        if choice.isdigit():
            choice = int(choice)

            if 1 <= choice <= len(MENU):
                return choice - 1
            else:
                print("Invalid choice. ")
                continue
                     
        else:
            print(Fore.RED + "❌ Please enter a valid number." + Style.RESET_ALL)
        
       
#*************************************************************************************

if  __name__ == "__main__":
    main_menu()
