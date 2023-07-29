# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
# This is a simple tip calculator that accepts meal cost and tip percentage and calculates the tip

def main():
    uInput = input("What is the answer to the Great Question of Life, the Universe and Everything? ").lower()
    
    match uInput:
        case "42" | "forty-two" | "forty two":
            print("Yes")
        case _:
            print("No")


main()