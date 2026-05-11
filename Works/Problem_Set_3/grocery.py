market = {}

while True:
    try:
        item = str(input("")).upper().strip()
        market[item] = market.get(item, 0) + 1

    except EOFError:
        break

for item in sorted(market):
    print(market[item], item)