names = []

for _ in range(3):
    #append adds object to the end of the list
    names.append(input("what's your name? "))

#sorted: Return a new list containing all items 
#from the iterable in ascending order (alphabet).
for name in sorted(names):
    print(f"hello, {name}")