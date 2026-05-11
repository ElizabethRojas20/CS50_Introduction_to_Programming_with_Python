import sys
import requests
import json


def main():
    bitcoin_v = bitcoin_value()
    quant = quantity()

    newamount = bitcoin_v * quant

    print(f"${newamount:,.4f}")

def bitcoin_value():
    response = requests.get("https://rest.coincap.io/v3/assets/bitcoin?apiKey=0c5784c0d1395cd7affb0ea9e8d01247703c8a9986a86185816026944a622db3")
    #print(json.dumps(response.json(), indent=2)) 

    o = response.json() #convierte la respuesta de la API en un diccionario
    for result in o["data"]: #recorre claves del diccionario
        if result == "priceUsd":
            value = float(o["data"][result])
            return value


def quantity():
    while True:
        try:
            if len(sys.argv) < 2:
                sys.exit("Missing command-line argument")

            elif len(sys.argv) > 2:
                sys.exit("Too many arguments")

            else:
                try:
                    amount = float(sys.argv[1])
                    return amount

                except ValueError:
                    sys.exit("Command-line argument is not a number")
        except requests.RequestException:
            break

main()