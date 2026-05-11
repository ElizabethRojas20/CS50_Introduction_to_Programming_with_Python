#n by 1
def main():
    print_column(3)

def print_column(height):
    for _ in range(height):
        print("#")

#or
#def print_column(height):
#    print("#/n" * height, end="")

main()

#1 by n
def mainn():
    print_row(4)

def print_row(widht):
    print("?" * widht)

mainn()

#n by n
def mainnn():
    print_square(3)

def print_square(size):
    #for each row in square
    for i in range(size):
        #for each brick in row
        for j in range(size):
            #print brick
            print("#", end="")
        print()

mainnn()