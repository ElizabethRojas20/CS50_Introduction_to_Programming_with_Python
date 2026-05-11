import inflect

namelist = []
p = inflect.engine()

while True:
    try:
        names = input("Name: ")
        namelist.append(names)

    except EOFError:
        print()
        break

print("Adieu, adieu, to", p.join(namelist))