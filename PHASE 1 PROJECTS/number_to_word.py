ones = {
        "0" : "zero",
        "1": "one", 
        "2": "two", 
        "3": "three", 
        "4" : "four", 
        "5" : "five", 
        "6" : "six", 
        "7" : "seven", 
        "8" : "eight",
        "9" : "nine",

        "10": "ten", 
        "20": "twenty", 
        "30": "thirty", 
        "40" : "forty", 
        "50" : "fifty", 
        "60" : "sixty", 
        "70" : "seventy", 
        "80" : "eighty",
        "90" : "ninty",

        "11": "eleven", "12": "twelve", "13": "thirteen",
        "14": "fourteen", "15": "fifteen", "16": "sixteen",
        "17": "seventeen", "18": "eighteen", "19": "nineteen"


    }

keys = list(ones.keys())

while True:

    number = (input("Enter a number to convert to word or q to quit: "))

    if number == "q":
        break

    l = len(number)

    if number in keys:
        print(ones[number])

    elif len(number) == 2 and not number.endswith('0'):
        nums = []

        for i, v in enumerate(number):
            nums.append(v)

        i = ones[nums[0]+"0"]
        v  = ones[nums[1]]

        print(f"{i}-{v}")

    elif len(number) == 3:

        nums = []

        for i, v in enumerate(number):
            nums.append(v)

        if number.endswith("00"):
            print(f"{ones[nums[0]]} hundred")

        elif nums[1] == "0":
            h = ones[nums[0]]
            v =  ones[nums[2]]

            print(f"{h} hundred {v}")

        elif nums[2] == "0":
            h = ones[nums[0]]
            v =  ones[nums[1]+"0"]

            print(f"{h} hundred {v}")

        else:

            h = ones[nums[0]]
            i =  ones[nums[1]+"0"]
            v =  ones[nums[2]]

            print(f"{h} hundred {i}-{v}")