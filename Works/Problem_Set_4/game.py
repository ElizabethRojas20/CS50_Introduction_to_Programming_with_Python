from random import randint

while True:
    try:
        n = int(input("Level: "))
        if n > 0:
            break #sale del bucle

    except ValueError:
        pass #repite el bucle

number = randint(1, n)

while True:

    while True:
        try:
            guess = int(input("Guess: "))
            if guess > 0:
                break

        except ValueError:
            pass

    if guess > number:
        print("Too large!")

    elif guess < number:
        print("Too small!")

    else:
        print("Just right!")
        break