# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
"""
a program that enables a user to place an order, prompting them for items, one per line,
until the user inputs control-c . 
After each inputted item, display the total cost of all items inputted thus far, 
prefixed with a dollar sign ($) and formatted to two decimal places. Treat the user’s input case insensitively. 
Ignore any input that isn’t an item. Assume that every item on the menu will be titlecased.
"""
def main ():
    menu = {
    "Baja Taco": 4.00,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
    
}
    
        
    order =[]
    bill = 0
    
    while True:
        try:
            item = input("Enter Item: ").strip().title()
            order.append(item)
            if item in menu:
                bill += menu[item]
                print("Total: $", bill)
        except KeyboardInterrupt:
            print("\n")
            print("Total: $", bill)
            break



if __name__ == "__main__":
    main()