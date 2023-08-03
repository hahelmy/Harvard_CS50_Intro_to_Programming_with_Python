# HARVARD University
# CS50 introduction to programming using python - Problem Set 4
# -------------------------------------------------------------
# A simple guessing game .. the user chooses a level (a random number will be generated between 1 and that number), then
# user would try to guess the number

import random

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    if level > 0:
        break

target = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    if guess > 0:
        if guess > target:
            print("Too large!")
        elif guess < target:
            print("Too small!")
        else:
            print("Just right!")
            break
    
    
