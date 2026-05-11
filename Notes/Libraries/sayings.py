def main():
    hello("world")
    goodbye("world")


def hello(name):
    print(f"hello, {name}")


def goodbye(name):
    print(f"goodbye, {name}")

#main()  #is going to run everything is we import sayings

if __name__ == "__main__": #it controls whether code runs immediately or only when the file is executed directly.
    main()
