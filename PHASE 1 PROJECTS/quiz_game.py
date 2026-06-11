import random

QUESTION_ANSWER_DICT = {
    "What does CPU stand for?": "central processing unit",
    "What does GPU stand for?": "graphics processing unit",
    "What does RAM stand for?": "random access memory",
    "What does PSU stand for?": "power supply unit",
    "What is the capital of France?": "paris",
    "Who wrote 'Romeo and Juliet'?": "william shakespeare",
    "What is the largest planet in our solar system?": "jupiter",
    "What is the chemical symbol for water?": "h2o",
    "What is 5 squared?": "25",
    "Who painted the Mona Lisa?": "leonardo da vinci",
    "What is the fastest land animal?": "cheetah",
    "Which gas do humans need to breathe?": "oxygen",
    "What is the capital of Japan?": "tokyo",
    "Who discovered gravity?": "isaac newton",
    "What is the smallest prime number?": "2",
    "Which ocean is the largest?": "pacific ocean",
    "What is the national language of Pakistan?": "urdu",
    "What is the boiling point of water in Celsius?": "100",
    "Who is known as the father of computers?": "charles babbage",
    "What is the square root of 64?": "8"
}


def play():
    while True:
        play = input("Do you want to play? (yes / no)  ")

        if play == "yes":
            print("Okay! Let's play.")
            return True
        
        elif play == "no":
            print("Good Bye..")
            return False

        else:
            print("Invalid input! Try Again.")
            continue
        


def main():
    correct = 0
    QUESTIONS_LENGTH = len(QUESTION_ANSWER_DICT.keys())

    if play():
        print(f"You will be asked {QUESTIONS_LENGTH} questions.")

        questions = list(QUESTION_ANSWER_DICT.items())
        random.shuffle(questions)

        for q,a in questions:
            answer = input(q).lower()

            if answer == a.lower():
                print("Correct!")
                correct += 1
            else:
                print("Wrong!")

        print(f"You got {correct} right. {correct}/{QUESTIONS_LENGTH }")

main()