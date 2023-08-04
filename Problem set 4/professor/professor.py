# HARVARD University
# CS50 introduction to programming using python - Problem Set 4
# -------------------------------------------------------------
# A program that outputs 10 addition questions and calculates the score .. 
# 3 levels are available (1,2 and 3 digits)

import random


def main():
    score = 0 # Total score accumulator
    games = 10 # number of questions generated
    level = get_level() # Get requested level from user
    
    while games > 0:
        x = generate_integer(level) # generate first number
        y = generate_integer(level) # generate second number
        z = x + y # calculate the correct answer

        
        trials = 3 # Three attempts are allowed then the correct answer will be printed
        while trials > 0:   
            try:
                answer = int(input(f"{x} + {y} = "))  # print the question
            except ValueError:
                break
            if answer == z: # user answered correctly
                trials = 0
                score += 1
            else: # user answered incorrectly
                print('EEE')
                trials -=1
                if trials == 0:
                    print(f"{x} + {y} = {z}") # print the correct answer if the user failed 3 times
        games -=1
    print(f"Total score: {score}") # Print the total score

def get_level(): # get the level number from user
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            level = 0
        if level in [1,2,3]:
             return level
        else:
             continue


def generate_integer(level): # generate a random number (number of digits for the questions set)
    if level == 1:
        return random.randint(1,10)
    elif level == 2:
        return random.randint(10,100)
    elif level == 3:
        return random.randint(100,1000)
    else:
        print("No such level")
        



if __name__ == "__main__":
    main()