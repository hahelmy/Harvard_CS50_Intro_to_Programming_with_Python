# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
"""
A program that prompts the user for a str in English and then outputs the “emojized” version of that str, 
converting any codes (or aliases) therein to their corresponding emoji.
"""

import emoji
import re

uInput = input("Input: ").split()
output =""

for i in range(0,len(uInput)):
    output += re.sub(r":.+:", emoji.emojize(uInput[i]), uInput[i]) + " "

print("Output: ",output)

