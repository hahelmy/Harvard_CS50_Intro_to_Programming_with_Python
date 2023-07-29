# HARVARD University
# CS50 introduction to programming using python - Problem Set 0
# -------------------------------------------------------------
# This is a simple tip calculator that accepts meal cost and tip percentage and calculates the tip


def main():
    # Get the amounts from the user and pass them to the appropriate functions for conversion
    dollars = dollars_to_float(input("How much was the meal? "))
    percent = percent_to_float(input("What percentage would you like to tip? "))
    
    # Calculates the tip amount
    tip = dollars * percent
    # Formats and prints the tip amount
    print(f"Leave ${tip:.2f}")

# Remove the $ sign and convert the str to float
def dollars_to_float(d):
    return float(d[1:])

# Romove the % symbol and return the percentage as a float
def percent_to_float(p):
    return(float(p[:-1])/100)


main()