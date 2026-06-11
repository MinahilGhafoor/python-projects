from imports import *


MENU_DICT = {"Add a Session: " : addSession,
             "View a Session " : viewSession,
             "Search a Session" : searchSession,
             "Delete a Session" : delSession,
             "quit" : quito}

def MENU():
    print("Wanna : ")

    options = list(MENU_DICT.keys())
    COUNT = 0


    while True:

        for idx in range(len(options)):
            print(f"{idx+1}. {options[idx]}")

        choice = input("Enter your choice: ")
        if choice.isdigit():
            choice = options[int(choice) - 1]
            MENU_DICT[choice]()
            
        else:
            print("Please enter a digit")

MENU()