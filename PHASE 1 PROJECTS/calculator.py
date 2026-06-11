OPERATORS = ["+", "-", "*", "/", "**"]

def welcome():
    print("Welcome to the MG CALCULATIONS.",end="\r")

    while True:
        play = input("Do you want to play? (yes / no)  ").lower()

        if play == "yes":
            print("Okay! Let's play.")
            return True

        elif play == "no":
            return False

        else:
            print("Incorrect input! Try Again.")

def add(list_to_add):
    add = 0

    for i in list_to_add:
        add += int(i)

    return add

def sub(list_to_sub):
    sub = int(list_to_sub[0])

    for i in list_to_sub[1:]:
        sub -= int(i)

    return sub

def mul(list_to_mul):
    mul = 1

    for i in list_to_mul:
        mul *= int(i)

    return mul

def div(list_to_div):
    div = list_to_div[0]

    for i in list_to_div[1:]:
        div /= int(i)

    return div

def choose_operator():
    while True:
        operator = input(f"Choose your operator {OPERATORS}  ")

        if operator not in OPERATORS:
            print("Incorrect Operator. Try Again!")
            continue

        return operator

def addition():
    print("We will keep asking numbers to add until you say Done.")
    current = []

    while True:
        number = input(f"Enter a number to add to {current} or write done to done :  ")
        if number.isdigit():
            current.append(int(number))
        
        elif number == "d":
            added = add(current)
            print(f"Your total is {added}")
            break

        else:
            print("Enter a number to add or done to get done.")

def subtraction():
    print("We will keep asking numbers to subtract until you say Done.")
    current = []

    while True:
        number = input(f"Enter a number to subtract  {current} or write done to done :  ")
        if number.isdigit():
            
            current.append(int(number))
        
        elif number == "d":
            subtracted = sub(current)
            print(f"Your total is {subtracted}")
            break

        else:
            print("Enter a number to add or done to get done.")

def multiplication():
    print("We will keep asking numbers to multiply until you say Done.")
    current = []

    while True:
        number = input(f"Enter a number to multiply to {current} or write done to done :  ")
        if number.isdigit():        
            current.append(int(number))
        
        elif number == "d":
            multiplied = mul(current)
            print(f"Your total is {multiplied}.")
            break

        else:
            print("Enter a number to add or done to get done.")

def division():
    print("We will keep asking numbers to divide until you say Done.")
    current = []

    while True:
        number = input(f"Enter a number to divide to {current} or write done to done :  ")
        if number.isdigit():

            if number == "0":
                print("0 is not used in division.")
                continue
            
            current.append(int(number))  
        
        elif number == "d":
            divided = div(current)
            print(f"Your total is {divided}.")
            break

        else:
            print("Enter a number to add or done to get done.")

def square():
    while True:
        num = input("Enter a number to square: ")
        if num.isdigit():        
            num = int(num)
            print(f"You get: {num * num}")
            break
        else:
            print("Enter a valid integer.")


def main():

    while True:
        if not welcome():
            print("GOOD BYE!")
            break

        operator = choose_operator()

        if operator == "+":
            addition()
        
        elif operator == "-":
            subtraction()

        elif operator == "*":
            multiplication()

        elif operator == "/":
            division()

        elif operator == "**":
            square()

main()