# HARVARD University
# CS50 introduction to programming using python - Problem Set 0
# -------------------------------------------------------------
# This is a simple script that asks the user to input some text
# and prints it back to the screen with '...' instead of a space 
# between words

def main():
    # # Propmt the user for input and then split it
    # uInput = input("Please type some text to be proccessed: ")
    # uInput = uInput.split()
    
    # # go throug the list and prints each item and add the '...' seperator unless it is the last item
    # for item in uInput:
    #     if uInput.index(item) == len(uInput)-1:
    #         print(item)
    #     else:
    #         print(item + '...' ,end='')
    
    ##########################################
    #      And this is a better version :)   #     
    ##########################################
    
    # Prompt the user for input and use the replace method
    uInput = input("Please type some text to be proccessed: ")
    print(uInput.replace(" ", "..."))
  
    



main()