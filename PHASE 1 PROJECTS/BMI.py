"""
BMI = weight in kg divided by height in meters squared.
BMI = weight / (height * height)
Results:

Below 18.5 = Underweight
18.5 to 24.9 = Normal
25 to 29.9 = Overweight
30 and above = Obese

You wanted age and gender too — those don't change the calculation, just add context to the output.
Now go. 🔥
"""

def main():
    while True:
        weight = input("Enter your weightin kg : ")
        try:
            weight = float(weight)
        except:
            print("Enter a valid number.")
            continue

        while True:

            height = input("Enter your height in cm : ")
            try:
                height = float(height) / 100
                break
            except:
                print("Enter a valid number.")
                continue


        BMI = weight / (height ** 2)

        if BMI < 18.5:
            print("Under weight.")
            break

        elif 18.5 < BMI < 24.9:
            print("Normal")
            break

        elif 24.9 < BMI < 29.9:
            print("Over weight")
            break

        elif BMI > 29.9:
            print("Obese")
            break

        else:
            print("huh")
            continue
        
main()  