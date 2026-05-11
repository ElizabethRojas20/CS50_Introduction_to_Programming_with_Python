#int, no decimal
x = int(input("What's x? "))
y = int(input("What's y? "))

print(x + y)

#compact, but not quite convenient
print(int(input("What's x? ")) + int(input("What's y? ")))

#float, has decimal point
x = float(input("What's x? "))
y = float(input("What's y? "))

print(x + y)

#round, round values, round(number[, ndigits])
z1 = round(x + y)        #approximates to the nearest integer
print(z1)

z2 = x/y
print(f"{z2:.2f}")      #shows 2 digits after the point


#calculator using def
def main():
    x1 = int(input("What's x? "))
    print("x squared is", square(x1))

def square(n):
    return pow(n, 2)

main()