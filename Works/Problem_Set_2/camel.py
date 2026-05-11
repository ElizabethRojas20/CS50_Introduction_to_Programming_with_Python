camelCase = str(input("camelCase: "))

snakeCase = ""

for letter in camelCase:
    if letter.isupper():
        snakeCase += "_" + letter.lower()
    else:
        snakeCase += letter

print(snakeCase)