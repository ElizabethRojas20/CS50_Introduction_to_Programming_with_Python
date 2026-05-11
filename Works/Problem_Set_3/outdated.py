month = {
    "january" : 1,
    "february" : 2,
    "march" : 3,
    "april" : 4,
    "may" : 5,
    "june" : 6,
    "july" : 7,
    "august" : 8,
    "september" : 9,
    "october" : 10,
    "november" : 11,
    "december" : 12
}

while True:
    date = str(input("Date: "))

    if "/" in date:
        try:
            x, y, z = date.split("/")
            x = int(x)
            y = int(y)
            z = int(z)

        except ValueError:
            continue

    elif "," in date:
        try:
            datere = date.replace(",", "")
            x, y, z = datere.split(" ")
            x = month[x.lower()]
            y = int(y)
            z = int(z)

        except (ValueError, KeyError):
            continue

    else:
        continue

    if 1 <= x <= 12 and 1 <= y <= 31:
        break

print(f"{z}-{x:02}-{y:02}")