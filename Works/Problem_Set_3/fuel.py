def main():
    frac = get_frac()
    print(frac)

def get_frac():
    while True:
        try:
            frac = str(input("Fraction: "))

            x, y = frac.split("/")

            x = int(x)
            y = int(y)

            perc = round((x / y) * 100)

            if x > y or x < 0 or y <= 0:
                continue

            perc = round((x / y) * 100)

            if perc >= 99:
                return "F"

            elif perc <= 1:
                return "E"

            else:
                return f"{perc}%"

        except (ValueError, ZeroDivisionError):
            continue
main()