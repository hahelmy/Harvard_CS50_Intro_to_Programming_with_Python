# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
"""
A program that prompts the user for items, one per line, until the user inputs control-c. 
Then output the user’s grocery list in all uppercase, sorted alphabetically by item, 
prefixing each line with the number of times the user inputted that item
"""
def main():
    
    list = {}
    
    while True:
        try:
            item = input("").lower().strip()
            if not item in list:
                list[item]=1
            else:
                list.update({item:int(list[item])+1})
            
        except KeyboardInterrupt:
            for item in sorted(list):
                print(list[item], item.upper())
            break
    

if __name__ == "__main__":
    main()