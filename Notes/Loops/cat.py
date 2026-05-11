# primero
i = 1

while i <= 3:
    print("meow")
    i += 1  #the same as i = i + 1

#segungo
for j in [0, 1, 2]:
    print("meow")

print("meow/n" * 3, end="")   

#tercero
while True:
    n = int(input("What's n? "))
    if n > 0:
        break

for _ in range(n):
    print("meow")

#cuarto
def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What's n?: "))
        if n > 0:
            break
    return n

def meow(n):
    for _ in range(n):
        print("meow")

main()