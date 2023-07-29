# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
#  A program that prompts the user for a greeting. 
#  If the greeting starts with “hello”, output $0. 
#  If the greeting starts with an “h” (but not “hello”), output $20.
#  Otherwise, output $100. 

def main():
    uInput = input("Greet me: ").strip().lower()
    
    if uInput[0:5]=='hello':
        print("$0")
    elif uInput[0] == "h":
        print("$20")
    else:
        print("$100")
    


main()