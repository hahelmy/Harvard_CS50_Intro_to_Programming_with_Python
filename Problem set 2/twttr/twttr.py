# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
# A program that prompts the user for a str of text 
# and then outputs that same text but with all vowels (A, E, I, O, and U) omitted, 
# whether inputted in uppercase or lowercase.

def main():
    uInput = input("Enter a string to shorten: ")
    
    for char in uInput:
        if char in ["o","O","a","A","i","I","e","E"]:
            uInput= uInput.replace(char,"")

    print (uInput)

if __name__ == "__main__":
    main()