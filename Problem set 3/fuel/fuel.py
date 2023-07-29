# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
"""
a program that prompts the user for a fraction, formatted as X/Y, wherein each of X and Y is an integer, 
and then outputs, as a percentage rounded to the nearest integer, how much fuel is in the tank. 
If, though, 1% or less remains, output E instead to indicate that the tank is essentially empty. 
And if 99% or more remains, output F instead to indicate that the tank is essentially full.

If, though, X or Y is not an integer, X is greater than Y, or Y is 0, instead prompt the user again. 
(It is not necessary for Y to be 4.) Be sure to catch any exceptions like ValueError or ZeroDivisionError.
"""
def main ():
    percentage()


def percentage():
    fraction = input("Fraction: ")
    up,down = fraction.split("/")
    

        
    try:
       
        result = round(int(up)/int(down)*100)
            
        if result >= 99:
            print("F")
        elif result <= 1:
            print("E")
        elif result > 100:
            percentage()
        else:
            print(f"{result} %")
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
        percentage()
    except ZeroDivisionError:
        print("Oops!  Division by Zero.  Try again...")
        percentage()

if __name__ == "__main__":
    main()