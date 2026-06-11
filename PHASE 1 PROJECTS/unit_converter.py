

def welcome():
    print("Welcome to the MG UNIT CONVERSIONS.")

    while True:
        play = input("Do you want to play? (yes / no)  ").lower()

        if play == "yes":
            print("Okay! Let's play.")
            return True

        elif play == "no":
            return False

        else:
            print("Incorrect input! Try Again.")

def get_num_for_conversion():
    print("You will be prompted to enter a number for conversion...")
    
    while True:
        num = input(f"Enter a number for conversion: ")
        try:
            return float(num)
        except ValueError:
            print("Invalid number.")


def length_conversion():
    
    while True:
        choice = input("Length conversions:\n1. KM to Miles\n2. Miles to KM\n3. Meters to Feet\n4. Feet to Meters\n5. Back <-------\n")

        if choice == "5":
            print("Okay")
            break

        elif choice == "1":
            number = get_num_for_conversion()
            print(f"{number} km = {number * 0.62} miles.")

        elif choice == "2":
            number = get_num_for_conversion()
            print(f"{number} miles = {number * 1.6} km.")

        elif choice == "3":
            number = get_num_for_conversion()
            print(f"{number} m = {number * 3.28} ft.")

        elif choice == "4":
            number = get_num_for_conversion()
            print(f"{number} ft = {number / 3.28} m.")

        else:
            print("Invalid Input. Try Again!")

def weight_conversion():
    while True:
        choice = input(f"Weight conversions:\n1. KG to Grams\n2. Grams to KG\n3. KG to Pounds(lb)\n4. Pounds to KG\n5. Back <--- ")

        if choice == "5":
            print("Okay")
            break 

        elif choice == "1":
            number = get_num_for_conversion()
            print(f"{number}kg = {number * 1000}g.")

        elif choice == "2":
            number = get_num_for_conversion()
            print(f"{number}g = {number / 1000}kg.")

        elif choice == "3":
            number = get_num_for_conversion()
            print(f"{number}kg = {number * 2.2}lb. ")

        elif choice == "4":
            number = get_num_for_conversion()
            print(f"{number}lb = {number / 2.2}kg.")

        else:
            print("Invalid Input. Try Again!")

def temperature_conversion():
    while True:
        choice = input(f"Temperature conversions:\n1. Celcius to Fahrenheit\n2. Fahrenheit to Celcius\n3. Celicus to Kelvin\n4. Kelvin to Celcius\n5. Back <----")

        if choice == "5":
            print("Okay")
            break

        elif choice == "1":
            number = get_num_for_conversion()
            fahrenheit = ((9 / 5) * number) + 32

            print(f"{number}°C = {fahrenheit}°F. ")

        elif choice == "2":
            number = get_num_for_conversion()
            celcius = (5 / 9) * (number - 32)

            print(f"{number}°F = {celcius}°C. ")

        elif choice == "3":
            number = get_num_for_conversion()
            kelvin = number + 273

            print(f"{number}°C = {kelvin}K. ")

        elif choice == "4":
            number = get_num_for_conversion()
            celcius = number - 273

            print(f"{number}K = {celcius}°C. ")

        else:
            print("Invalid Input. Try Again!")

def main():

    while True:
        choice = input("What do you want to convert? (1. Length, 2. Weight, 3. Temperature) (1, 2, 3) or (q to quit):  ").lower()

        if choice == "q":
            print("GoodBye Curious Converter !")
            break

        elif choice == "1":
            length_conversion()

        elif choice == "2":
            weight_conversion()

        elif choice == "3":
            temperature_conversion()

        else:
            print("Invalid Choice. Try Again!")

if __name__ == "__main__":
    main()