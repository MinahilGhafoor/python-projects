
def getValidInput(prompt):

    while not (value := input(prompt).strip()):
        print("❌ Cannot be empty!")
    return value

