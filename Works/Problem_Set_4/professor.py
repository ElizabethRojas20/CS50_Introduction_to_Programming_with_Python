from random import randint

def main():
    note = 0
    excercises = 0

    level = get_level()

    while excercises < 10:
        n1 = generate_integer(level)
        n2 = generate_integer(level)

        error = 0

        while error < 3:
            try:
                result = int(input(f"{n1} + {n2} = "))

            except ValueError:
                #we put result -1, in case we put something incorrect
                #-10 will always be incorrect, so it will break the bucle and print EEE
                result = -10

            if result == n1 + n2:
                note += 1
                break

            else:
                print("EEE")
                error += 1

        if error == 3:
            print(f"{n1} + {n2} = {n1 + n2}")

        excercises += 1

    print(f"Score: {note}")

def get_level():
    while True:
        try:
            level = int(input("Level: "))

            if level == 1 or level == 2 or level == 3:
                return level

        except ValueError:
            pass

def generate_integer(level):
    if level == 1:
        return randint(0, 9)

    elif level == 2:
        return randint(10, 99)

    elif level == 3:
        return randint(100, 999)

    else:
        raise ValueError

if __name__ == "__main__":
    main()