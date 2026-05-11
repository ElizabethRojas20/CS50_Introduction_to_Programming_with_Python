def hello():
    print("Hello,")

name = input("What's your name? ")
hello()
print(name)


def hello(to):
    print("Hello,", to)

name = input("What's your name? ")
hello(name)


def hello(to="world"):
    print("Hello,", to)

hello()
name = input("What's your name? ")
hello(name)