import os
import platform
import json
#=======================================================================================================================
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def clearScreen():
    try:
        if platform.system() == "Windows":
            os.system("cls")
        else:
            os.system("clear")

    except Exception as e:
        print("Could not clear screen:", e)
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def welcome():
    print("WELCOME TO MG CONTACT BOOK.....")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def addContact():
    with open('contacts.json', 'r') as f:
        data = json.load(f)

    name = input("Enter contact name: ")
    phone = input("Enter contact number: ")
    email = input("Enter contact email: ")

    data[name] = {"phone" : phone, "email" : email}

    with open('contacts.json', 'w') as f:
        json.dump(data, f)
        print(f"Contact {name} saved successfully.")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def viewContacts():
    with open('contacts.json', 'r') as f:
        data = json.load(f)

        for i,v in data.items():
            print(f"Contact name : {i} ,  Phone number : {v["phone"]} , Email : {v["email"]}")
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def searchName():
    with open('contacts.json', 'r') as f:
        data = json.load(f)

    contacts = []

    for i in data:
        contacts.append(i)

    while True:
        search = input("Enter a name to search:  ")

        if search in contacts:
            print(data[search])
            break

        else:
            print("No such contact or try checking your spelling mistakes.")        
        
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def delContact():
    with open('contacts.json', 'r') as f:
        data = json.load(f)

    for i,v in data.items():
            print(f"Contact name : {i} ,  Phone number : {v["phone"]} , Email : {v["email"]}")

    while True:
        name = input("Enter a contact name to delete: ")

        if name in list(data.keys()):
            del data[name]
            print("O! Found it. I am deleting.")
        else:
            print("No such contact or try checking your spelling mistakes.")

        with open("contacts.json", "w") as f:
            json.dump(data, f)
            print(f"Deletion of {name} seccusffuly.")
            break
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
def quito():
    print("Well. Good Bye!. Kam sa mi da!")
    quit()
#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

CMD_DICT = {"1" : addContact, "2" : viewContacts, "3" : searchName, "4" : delContact, "5" : quito}


def main():
    welcome()
    while True:
        choice = input("Wanna:\n 1. Add Contact\n2. View Contacts\n3. Search by name\n4. Delete Contact\n5. Quit\n")

        if choice in CMD_DICT:
            CMD_DICT[choice]()
        
        else:
            print("Invalid choice try again")

#++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
main()