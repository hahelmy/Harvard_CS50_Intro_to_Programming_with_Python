# HARVARD University
# CS50 introduction to programming using python - Problem Set 4
# -------------------------------------------------------------
# A program that queries the API for the CoinDesk Bitcoin Price Index and reads the returned json, 
# then calculates the price of the dollar value of the bitcoin amound entered as an argv

import requests
import sys

def main():
    if len(sys.argv) > 2:
        print("Too many arguments")
    elif len(sys.argv) == 1:
        print("Missing argument")
    else:
        try:
            dollar = float(sys.argv[1])
            rate = get_rate()
            amount = dollar * rate
            print (f"${amount:,.4f}")
        except ValueError:
            print("Argument is not a number")
            sys.exit
    
    
def get_rate():
    try:
        r = requests.get('https://api.coindesk.com/v1/bpi/currentprice.json')
        content = r.json()
        return float(content['bpi']['USD']['rate_float'])
    except requests.RequestException:
        print("Connection Error")

if __name__ == "__main__":
    main()

