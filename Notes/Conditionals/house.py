name = input("What's your name? ")

#first case
if name == "Harry" or name == "Hermione" or name == "Ron":
    print("Gryffindor")

elif name == "Draco":
    print("Slytherin")

else:
    print("Who?")


#second case, using match
match name:
    case "Harry":
        print("Gryffindor")
    case "Hermione":
        print("Gryffindor")
    case "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case __:
        print("Who?")


#third case, one line
match name:
    case "Harry" | "Hermione" | "Ron":
        print("Gryffindor")
    case "Draco":
        print("Slytherin")
    case __:
        print("Who?")