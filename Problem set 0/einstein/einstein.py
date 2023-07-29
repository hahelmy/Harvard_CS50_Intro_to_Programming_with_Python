# HARVARD University
# CS50 introduction to programming using python - Problem Set 0
# -------------------------------------------------------------
# This is a simple script that asks the user to input the mass
# and prints the energy using the E=M*C^2 formula


def main():
    # Prompt the user for input and pass it to the emc2 function then prints the result
    uInput = input("Please enter tha mass to calculate the energy: ")
    print(emc2(int(uInput)))

# function to return the result of the E=M*C^2 formula
def emc2(mass):
    return mass * pow(300000000,2)




main()