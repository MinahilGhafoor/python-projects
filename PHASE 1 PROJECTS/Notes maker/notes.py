import json


#==============================================================================

def newNote():
    title = input("Title:   ")
    text = input(f"Text:    ")
    
    with open("notes.json", "r") as f:   
        notes = json.load(f)

    notes[title] = text

    with open("notes.json", "w") as f:   
        json.dump(notes, f)

def viewNote():
    with open("notes.json" , "r") as f:
        loaded = json.load(f)
        
        keys = list(loaded.keys())

        for i in keys:
            print(f"{i} ==== {loaded[i]}")


def delNote():
    with open("notes.json" , "r") as f:
        loaded = json.load(f)
        keys = list(loaded.keys())

    for i in keys:
        print(f"{i} ==== {loaded[i]}")

    while True:
        choice = input("Enter a note's title to delete: ")
        if choice in keys:
            print(f"Note '{choice}' founded!")
            del loaded[choice]
            keys.remove(choice)
            print(f"Note '{choice}' has been deleted successfully.")
            break

        else:
            print("Cant find the precious note.")

    with open("notes.json" , "w") as f:
        json.dump(loaded, f)
    

def quitNoteSense():
    print("Okay! Quit is your choice.")
    print("Bye")
    quit()

cmd_dict = {"1" : newNote, "2" : viewNote, "3" : delNote, "4" : quitNoteSense}

#===========================================
#===========================================
def main():
    print("Welcome to NoteSense")

    while True:
        choice = input(f"Do you want to:\n1. Write a note.\n2. View all notes.\n3. Delete a note.\n4. Quit NoteSense\n")

        if choice in cmd_dict:
            cmd_dict[choice]()
        else:
            print("Invalid Input!")


    
if __name__ == "__main__":
    main()