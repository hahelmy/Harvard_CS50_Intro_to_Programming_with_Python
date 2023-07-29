# HARVARD University
# CS50 introduction to programming using python - Problem Set 2
# -------------------------------------------------------------
# A program that prompts the user for the name of a variable in camel case 
# and outputs the corresponding name in snake case
def main():
     camel_case = input("Camelcase: ")
     
    #  cap_indecies = []
     
    #  for i in range(len(camel_case)):
    #      if camel_case[i].isupper():
    #          cap_indecies.append(i)
             
      
    #  if len(cap_indecies) == 0:
    #     print(f"Snakecase: {camel_case.lower()}")
    #  elif len(cap_indecies) == 1:
    #      st1 = camel_case[:int(cap_indecies[0])].lower()
    #      st2 = camel_case[int(cap_indecies[0]):].lower()
    #      print(f"Snakecase: {st1}_{st2}",end="",sep="")
    #  elif len(cap_indecies) == 2:
    #      st1 = camel_case[:int(cap_indecies[0])].lower()
    #      st2 = camel_case[int(cap_indecies[0]):int(cap_indecies[1])].lower()
    #      st3 = camel_case[int(cap_indecies[1]):].lower()
    #      print(f"Snakecase: {st1}_{st2}_{st3}",end="",sep="")
    
    ##############################################################
    #            A much simpler way to do the same               #
    ##############################################################
     for char in camel_case:
        if char.isupper():
            print("_" + char.lower() , end="")
        else:
            print(char,end="")
     print()
main()