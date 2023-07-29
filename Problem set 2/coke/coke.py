# HARVARD University
# CS50 introduction to programming using python - Problem Set 2
# -------------------------------------------------------------
# A program that prompts the user to insert a coin, one at a time, 
# each time informing the user of the amount due. 
# Once the user has inputted at least 50 cents, 
# output how many cents in change the user is owed.
# Assume that the user will only input integers, and ignore any integer that isn’t an accepted denomination


def main():
   
    print("Insert 50c: ")
   
    balance = 50
   
    while True:
        coin = int(input("Insert coin (25c,10c or 5c) :"))
        
       
        if coin in (25,10,5) and coin <= balance:
            balance -= coin
            print (f"Balance: {balance}")
            if balance == 0:
               break


main()