import random
import time

def welcome():
    print("Welcome to dice rolling stimulator.")

def roll_dice():
    return random.randint(1, 6)

def end_program():
    print("Good Bye!")


def number_of_dice_to_roll():
    while True:
        roll_num = input("How many dice you want to roll at once: ")

        if roll_num.isdigit():
            roll_num = int(roll_num)
            if roll_num > 0:
                return roll_num
            else:
                print("Please enter a digit greater than 0.")
                continue
        else:
            print("Please enter a valid integer")

def main():
    welcome()

    Sum = 0

    while True:
        roll = input("Do you want to roll the dice: (y/n) ").upper()
        
        if roll == "Y":
            roll_num = number_of_dice_to_roll()
            result = 0

            for _ in range(roll_num):
                face = roll_dice()
                print(f"You rolled a {face}.")
                time.sleep(1)
                result += face

            time.sleep(1)
            print(f"Result: {result}")
            Sum += result

        elif roll == "N":
            print(f"Your total is: {Sum}")
            time.sleep(1)
            end_program()
            break

        else:
            print("Invalid Input. ")

if __name__ == "__main__":
    main()