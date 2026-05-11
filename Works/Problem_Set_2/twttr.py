vowels = ["a", "e", "i", "o", "u", "A", "E", "I", "O", "U"]

twitter = str(input("Input: "))

twttr = ""

for letter in twitter:
    if letter in vowels:
        pass
    else:
        twttr += letter

print(twttr)