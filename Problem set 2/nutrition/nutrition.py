# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
#a program that prompts consumers users to input a fruit (case-insensitively) 
# and then outputs the number of calories in one portion of that fruit, per the FDA’s poster for fruits



def main ():
    
    facts ={
    'apple':130,
    'avocado':50,
    'banana':110,
    'cantaloupe':50,
    'grapefruit':60,
    'grapes':90,
    'Honeydew Melon':50,
    'kiwifruit':90,
    'lemon':15,
    'lime':20,
    'nectarine':60,
    'orange':80,
    'peach':60,
    'pear':100,
    'pineapple':50,
    'plums':70,
    'strawberries':50,
    'sweet cherries':100,
    'tangerine':50,
    'watermelon':80
    
}
    fruit = input("Fruit: ").lower().strip()
    
    if not fruit in facts:
        exit()
    else:
        print(f"Calories: {facts[fruit]}")
    
 

if __name__ == "__main__":
    main()







