#Author: Sovial Sonzeu

# Resources:
# https://www.udacity.com/blog/2021/09/create-a-timer-in-python-step-by-step-guide.html
# https://docs.python.org/3/library/os.html
# https://www.programiz.com/python-programming/methods/string/casefold
# https://www.quizbreaker.com/trivia-questions

import random
import os
import time



collection =  {
    "What does “www” stand for in a website browser?": "World Wide Web",
    "How long is an Olympic swimming pool (in meters)?": "50 meters",
    "What countries made up the original Axis powers in World War II?": "Germany, Italy, and Japan",
    "Which country do cities of Perth, Adelade & Brisbane belong to?": "Australia",
    "What is the rarest M&M color?": "Brown",
    "What was the first soft drink in space?": "Coca Cola",
    "How many states are in the United States of America?": "50",
    "When Walt Disney was a child, which character did he play in his school function?": "Peter Pan",
    "Who has won more tennis grand slam titles, Venus Williams or Serena Williams?": "Serena Williams",
    "Dump, floater, and wipe are terms used in which team sport?": "Volleyball",
    "How many points did Michael Jordan score on his first NBA game?": "16",
    "How many colors are there in the rainbow?": "7",
    "Who was the first president of the United States?": "George Washington",
    "What's the city with the most diversity in terms of language?": "New York City",
    "Havana is the capital of what country?": "Cuba",
    "What is the loudest animal on Earth?": "Sperm Whale",
    "What is a group of crows called?": "Murder",
    "What type of matter are atoms most tightly packed?": "Solids",
    "What is the nearest planet to the sun?": "Mercury",
    "True or False - Pluto is an official planet in the solar system": "False",
    "Area 51 is located in which U.S. state?": "Nevada",
    "What is Earth's largest continent?": "Asia",
    "How many hearts does an octupus have?": "3",
    "How many NBA championships did Kobe Bryant win?": "5"
}

def triviaGame(rounds):
    score = 0
    correctAnswer = False
    for i in range(rounds):
        correctAnswer = False
        os.system("clear")
        question = random.choice(list(collection))
        for i in range(2):
            answer = str(input(f"{question} \n"))

            if answer.lower() == collection[question].lower():
                score += 100
                print(f"\nCorrect! Your score now is {score}")
                correctAnswer = True
                break
            else:
                print("\nWrong answer, you have one more try\n" if i == 2 else "Wrong answer\n")

        if correctAnswer == False:
            print(f"\n\nThe correct answer was {collection[question]}.")

            response = input(f"Did you enter something similar to {collection[question]}? If yes, please type \"y\", else type \"n\"\n")
            while True:
                if response == 'y':
                    score += 100
                    print(f"Ok, your score is updated and is now {score}")
                    break
                elif response == 'n':
                    score -= 100
                    print(f"Ok, your score is updated and is now {score}. Loading next question...")
                    break
                else:
                    response = input("\nPlease enter a valid option\n")
        
        del collection[question]
        time.sleep(2)

    print(f"""\n\nYour final score was {score}. 
Thanks for playing!""")

# ------------------------------------ #
while True:
    try:
        rounds = int(input("How many rounds would you like the game to be?\n"))
        break
    except:
        print("That is an invalid entry, please enter a number.")

print("\nOk, you will have two attempts for each question. Good luck and have fun!")
time.sleep(4)
triviaGame(rounds)
