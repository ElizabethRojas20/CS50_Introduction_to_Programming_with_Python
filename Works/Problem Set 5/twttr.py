vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

def main():
    word = str(input("Input: "))
    print(shorten(word))

def shorten(word):
    twttr = ""

    for letter in word:
        if letter in vowels:
            pass
        else:
            twttr += letter
    
    return twttr

if __name__ == "__main__":
    main()