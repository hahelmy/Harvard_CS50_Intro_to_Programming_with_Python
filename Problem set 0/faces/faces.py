# HARVARD University
# CS50 introduction to programming using python - Problem Set 0
# -------------------------------------------------------------
# This is a simple script that asks the user to input some text
# and prints it back to the screen after converting emoticons to emojies 

def main():
    # prompt the user to input some text and pass it the the conver() function
    print(convert(input("Please enter some text to convert emoticons to emojies: ")))

# This function searches the string for the smiley and sad emoticons and replaces them with
# the maching emojies
def convert(text):
    text = text.replace(":)", "🙂")
    text = text.replace(":(", "🙁")
    
    return text

main()
    