import json

def loadCard():
    with open('card.json', "r") as f:
        data = json.load(f)
    return data

def writeCard(data, card,answer):
    data[card] = answer

    with open('card.json', 'w') as f:
        json.dump(data, f)


def addCard():
    data = loadCard()

    card = input("Type card question: ").lower()
    answer = input("Type card answer: ").upper()

    writeCard(data, card,answer)

def studyCard():
    data = loadCard()
    correct = 0

    for q, a in data.items():
        answer = input(f"{q}:  ").upper()

        if answer == a:
            print("Correct! ✅")
            correct += 1
        else:
            print("Wrong!")

    total_questions = list(data.keys())
    print(f"Score: {correct} / {len(total_questions)}")

def delCard():
    data = loadCard()

    for i in enumerate(data.items(), start=1):
        print(i)

    questions = list(data.keys())

    while True:
        card = input("Enter a card number to delete:  ")

        if card.isdigit():
            card = int(card)
        else:
            print("Enter a valid integr.")
            continue

        del data[questions[card - 1]]
        break

    with open('card.json', 'w') as f:
        json.dump(data, f)


def quitCard():
    print("Okay your choice. I respect.")
    print("Bye!")
    quit()

cmd_dict = {"1" : addCard, "2" : studyCard, "3" :  delCard, "4" : quitCard}

def main():
    print("Welcome to Flash Card Ship.")

    while True:
        choice = input(f"Do you want to:\n1. Add a card.\n2. Study Cards..\n3. Delete a card.\n4. Quit Flash Card Ship\n")

        if choice in cmd_dict:
            cmd_dict[choice]()
        else:
            print("Invalid Input!")

if __name__ == "__main__":
    main()