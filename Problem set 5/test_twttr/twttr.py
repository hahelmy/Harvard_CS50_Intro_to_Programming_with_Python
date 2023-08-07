def main():
    print(shorten(input("Enter a phrase to shorten: ")))
    

def shorten(word):
    word = word.lower()
    for char in word:
        if char in ["o","O","a","A","i","I","e","E"]:
            word= word.replace(char,"")
    return word


if __name__ == "__main__":
    main()