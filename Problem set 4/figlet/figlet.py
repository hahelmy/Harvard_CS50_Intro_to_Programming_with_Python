# HARVARD University
# CS50 introduction to programming using python - Problem Set 4
# -------------------------------------------------------------
"""
A program that:

Expects zero or two command-line arguments:
Zero if the user would like to output text in a random font.
Two if the user would like to output text in a specific font, 
in which case the first of the two should be -f or --font, and the second of the two should be the name of the font.
Prompts the user for a str of text.
Outputs that text in the desired font.
If the user provides two command-line arguments and the first is not -f or --font 
or the second is not the name of a font, the program should exit via sys.exit with an error message.
"""

from pyfiglet import Figlet
import sys
import random

figlet = Figlet()

fonts = figlet.getFonts() # Gets a list of available fonts



if len(sys.argv) == 3: # Checks if a font was passed as an argument
    if sys.argv[1] == '-f' or sys.argv[1] == '--font': # checks the syntax
        
        if sys.argv[2] in fonts: # Check if the font is valid
            figlet.setFont(font=sys.argv[2])
            uInput = input("Input: ") # Get the string to apply the font to
            print(figlet.renderText(uInput)) # Prints the output
        else:
            print("No such font !") # Error .. If the choosen font does not exist
            sys.exit()
    else:
        print("Wrong syntax !") # Error .. If the syntax is wrong
        sys.exit()     
elif len(sys.argv) == 1: # if no font was passed outputs a random font
    figlet.setFont(font=random.choice(fonts))
    uInput = input("Input: ") #Get the string to apply the font to
    print(figlet.renderText(uInput))# Prints the output
else:
    print("Too many arguments !") # Error .. If more than two arguemts were passed


