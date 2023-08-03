# HARVARD University
# CS50 introduction to programming using python - Problem Set 4
# -------------------------------------------------------------
"""
A program that prompts the user for names, one per line, until the user inputs control-c. Assume that the user will input
at least one name. Then bid adieu to those names, separating two names with one and, 
three names with two commas and one and, and names with commas and one and
"""
import inflect
p = inflect.engine()

ls = []

while True:
    try:
        ls.append(input("Enter a Name: "))
    except KeyboardInterrupt:
        break
    
out = p.join(ls)

print("\n\nAdieu, adieu, to",out)