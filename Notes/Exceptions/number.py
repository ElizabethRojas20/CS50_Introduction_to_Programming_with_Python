#handling the ValueError with "try, except"
try:
    x = int(input("What's x? "))

except ValueError:
    print("x is not an integer")

else:
    print(f"x is {x}")

#if something is not right, it takes de "except" case
#but if anything is wrong, the exception isn't valid,
#so it goes to the "else" case

while True:
    try:
        x = int(input("What's x? "))
        #we can put the "break" here too, and delete the "else"

    except ValueError:
        print("x is not an integer")

    else:
        break  #breaks out of the loop

print(f"x is {x}")

#we can try until the input is an integer

#-----------
def main():
    x = get_int("What's x? ")
    print((f"x is {x}"))

def get_int(prompt):
    while True:
        try:
            return int(input(prompt))
            #less obvious 

        except ValueError:
            pass #we just ignore it
main()