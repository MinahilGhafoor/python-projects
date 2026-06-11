import json
from datetime import datetime
#**********************************************************************
def loadJson():
    with open("notes.json", "r") as f:
        data = json.load(f)
    return data

def getDate():
    now = datetime.now()
    return now.date()

def subjectName():
    while True:
        subject = input("Enter a subject name: ").strip()

        if subject == "":
            print("Subject name is compulsory.")
            continue
    
        return subject

def sessionDuration():
    while True:
        duration = input("Enter a subject's study duration in minutes : ")

        if duration.isdigit():
            return int(duration)

        print("Enter duration in minutes(number).")
        continue

def sessionNotes():

    notes = []
    while True:
        note = input("Wanna add notes: (y/n) ")

        if note == "y":
            text = input("Enter notes here: ")
            notes.append(text)

        elif note == "n":
            print("Fair Enough! No notes. Bye")
            return notes

        else:
            print("Invalid Try Again.")

def writeJson(data):
    with open("notes.json", "w") as f:
        json.dump(data, f)
#**********************************************************************
def addSession():
    data = loadJson()
    print("You want to add a Session.")

    date = getDate() 
    subject = subjectName()
    duration = sessionDuration()
    notes = sessionNotes()

    if not date in data:
        data[date] = []

    data[date].append({"Subject" : subject, "Duartion" : duration, "Notes" : notes})

    writeJson(data)

def viewSession():
    data = loadJson()

    print("__________")
    print()
    for date, val_list in data.items():
        print(f"Date: {date}")
        for session in val_list:          
            for key, value in session.items():
                print(key, "|", value)

            print("__________")
            print()

def searchSession():
    data = loadJson()
    sessions = []
    for date, session in data.items():
        for i in session:
            sessions.append((date,i))

    while True:
        subject = input("Enter subject name to search: ").upper()
        for i in sessions:
            date, session = i
            
            if session['subject'].upper() == subject:
                print("Found it!")

                print("__________")
                print()
                print(f"Date: {date}")  
                for key, value in session.items():                  
                    print(key, "|", value)

                print("__________")
                print()
                
                break
        else:
            print(f"No such subject as {subject}")
            continue
        break

    

def delSession():
    data = loadJson()
    INDEX = 0
    sessions, length = [],[]

    print("__________")
    print()
    for date, val_list in data.items():
        for session in val_list: 
            INDEX += 1   
            print(f"{INDEX}. Date: {date}")
                  
            for key, value in session.items():
                print(key, "|", value)

            sessions.append((date, session))

            print("__________")
            print()


    while True:
        print("Enter to delete: ")
        for i in range(len(sessions)):
            print(f"{i+1} | ", end="")

        print(">>>>>> ",end="")
        choice = input()

        if choice.isdigit():
            choice = int(choice) - 1
            
            for i in range(len(sessions)):
                length.append(i)

            if choice in length:

                date, session = sessions[choice]

                data[date].remove(session)
                print(f'Session "{session}" from {date} has been deleted successfully.')

                writeJson(data)
                break
            else:
                print("Invalid Choice.")
            
        else:
            print("Please enter a number.")
            continue


def quito():
    print("OH So decided to quit.... Makes me sad but dont worry.  Bye!")
    quit()