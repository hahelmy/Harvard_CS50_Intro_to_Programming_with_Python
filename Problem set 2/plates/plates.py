# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
'''
request a vanity license plate for your car, with your choice of letters and numbers instead of random ones. Among the requirements, though, are:

“All vanity plates must start with at least two letters.”
“… vanity plates may contain a maximum of 6 characters (letters or numbers) and a minimum of 2 characters.”
“Numbers cannot be used in the middle of a plate; they must come at the end. 
For example, AAA222 would be an acceptable … vanity plate; AAA22A would not be acceptable. 
The first number used cannot be a ‘0’.”
“No periods, spaces, or punctuation marks are allowed.”

'''
def main():
    if is_valid(input("Enter plate number: ")):
        print("Valid")
    else:
        print("Invalid")


# Check if lenght is valid
def length(plate):
    if 2 <= len(plate) <= 6:
        return True
    else:
        print("Plates may contain a maximum of 6 characters and a minimum of 2 characters")
        return False

# Check if first two chars are not numbers   
def pre_num(plate):
    if not plate[0].isnumeric() and not plate[1].isnumeric():
            return True
    else:
        print("Plates must start with at least two letters.")
        return False
    
    
# check for numbers in the middle   
def mid_num(plate):
    index = 0
    for char in plate:
        if char.isnumeric():
            if index+1 <= len(plate)-1:
                if not plate[index+1].isnumeric():
                    print("Numbers cannot be used in the middle of a plate.")
                    return False
        index+=1         
    return True

# check if the first digit is zero
def begin_zero(plate):
    digits = []
    for char in plate:
        if char.isnumeric():
            digits.append(char)
         
    if digits:
        if digits[0] == '0':
            print("The first number used cannot be a ‘0’.")
            return False
        else:
            return True
        
# check for non alpha num characters
def is_alph_num(plate):
    for char in plate:
        if not char.isalnum():
            print("No periods, spaces, or punctuation marks are allowed.")
            return False        
        
    return True
        
def is_valid(plate):
    
    if is_alph_num(plate) and length(plate) and pre_num(plate) and mid_num(plate) and begin_zero(plate):
        return True
    else:
        return False

if __name__ == "__main__":
    main()