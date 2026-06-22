import string
import secrets

####################################################################
def generatePassword():

    LETTERS = string.ascii_letters if wanna_add_letters() else ""
    DIGITS = string.digits if wanna_add_digits() else ""
    PUNCTUATION = string.punctuation if wanna_add_punctuation() else ""

    CHARACTERS = LETTERS + DIGITS + PUNCTUATION

    if not CHARACTERS:
        return "❌ Select at least one character type!"
    

    LENGTH = pwdLength() if (LENGTH := pwdLength()) > 5 else print("Invalid " if LENGTH >= 0 else print("Write a number"))
    return ''.join(secrets.choice(CHARACTERS) for _ in range(1, LENGTH) )

def pwdLength():

    while not (length := input("Enter a pwd length: ")).isdigit(): print("❌ Invalid! Numbers only!")
    length = int(length)
    return length 

def wanna_add_letters():
    
    while (letters := input("Wanna add alphabets? in password (y/n): ").upper()) not in {"Y", "N"}: print("❌ Invalid!")
    return letters == "Y"

def wanna_add_digits():
    
    while (digits := input("Wanna Add Numbers in password (y/n): ").upper()) not in {"Y", "N"}: print("Invalid!")
    return digits == "Y"

def wanna_add_punctuation():


    while (punc := input("Wanna add punctuation in password (y/n): ").upper()) not in {"Y", "N"}: print("Invalid!")
    return punc == "Y" 

##################################################################
