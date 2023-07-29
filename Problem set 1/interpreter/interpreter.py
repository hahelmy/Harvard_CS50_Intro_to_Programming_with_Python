# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
# A a program that prompts the user for an arithmetic expression 
# and then calculates and outputs the result as a floating-point value formatted to one decimal place

def main():
    x,y,z = input("Enter Expression: ").split()
    x = int(x)
    z = int(z)
    
    match y:
        case "+":
            print(round(float(x+z),2))
        case "-":
            print(round(float(x-z),2))
        case "*":
            print(round(float(x*z),2))
        case "/":
            print(round(float(x/z),2))
        case _:
            print("Unknown operator..")

main()