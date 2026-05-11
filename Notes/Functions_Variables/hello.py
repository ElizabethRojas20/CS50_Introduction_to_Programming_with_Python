# functions, calculates and returns a value
# arguments, values passed into a function
# side effects, changes something outside the function

print("Hello, world")

# return values
# variables, can be used for pseudocode


name1 = input("What's your name? ")
print("Hello, " + name1)


name2 = input("What's your name? ")
print("Hello, ", end="")
print(name2)


name3 = input("What's your name? ")
print(f"Hello, {name3}")


#name4 = name4.strip()           Remove whitespace from str
#name4 = name4.capitalize()      Capitalize user's name
#name4 = name4.strip().capitalize()
name4 = input("What's your name? ").strip().capitalize()
print(f"Hello, {name4}")


#name4 = name4.strip()           Remove whitespace from str
#name4 = name4.title()           Capitalize each word
#name4 = name4.strip().title()
name4 = input("What's your name? ").strip().title()
print(f"Hello, {name4}")