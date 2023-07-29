
# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
# A program that prompts the user for a time and outputs whether it’s breakfast time, lunch time, or dinner time
def main():
      
    time = convert(input("Please Enter time: "))
    
  
    if 7 <= time <= 8 :
        print("breakfast time")
    elif 12 <= time <= 13 :
        print("lunch time")
    elif 18 <= time <= 19 :
        print("dinner time")
    else:
        pass

def convert(time):
    h , m= time.split(sep=":")
    return int(h) + int(m)/60


if __name__ == "__main__":
    main()