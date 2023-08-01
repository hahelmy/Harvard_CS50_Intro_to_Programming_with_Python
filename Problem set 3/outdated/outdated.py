# HARVARD University
# CS50 introduction to programming using python - Problem Set 1
# -------------------------------------------------------------
"""
A program that prompts the user for a date, anno Domini, in month-day-year order, 
formatted like 9/8/1636 or September 8, 1636. Then output that same date in YYYY-MM-DD format. 
If the user’s input is not a valid date in either format, prompt the user again. Assume that every month has no more than 31 days; no need to validate whether a month has 28, 29, 30, or 31 days.
"""

def main():
    temp = []
    months = [
    "January",
    "February",
    "March",
    "April",
    "May",
    "June",
    "July",
    "August",
    "September",
    "October",
    "November",
    "December"
]
    uInput = input("Enter date: ").strip()

    if not uInput[0].isnumeric():
        temp = uInput.split(" ")
        m = int(months.index(temp[0]))+1
        d = temp[1].strip()
        d = d[:-1]
        y = temp[2].strip()
    else:
        m,d,y = uInput.split("/")

    print(f"{y}-{str(m).zfill(2)}-{d.zfill(2)}")


if __name__ == "__main__":
    main()