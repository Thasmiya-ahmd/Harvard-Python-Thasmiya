import requests
import sys

def main():
    try:
        num=float(sys.argv[1])
    except IndexError:
        sys.exit("Missing Command-line argument")
    except ValueError:
        sys.exit("Command-line argument is not a number")

    try:
        request=requests.get("http://rest.coincap.io/v3/assets/bitcoin?apiKey=f696c8ba43ecbabf835df95e702946e422f8eace1b84720dbae6e0dfe2e2a929")
        data=request.json()
        price=float(data["data"]["priceUsd"])
        print(f"${price*num:,.4f}")
    except requests.RequestException:
        print("API request failed")
    

if __name__=="__main__":
    main()