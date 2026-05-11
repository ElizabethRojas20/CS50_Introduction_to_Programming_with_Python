#First we take the user's input
text = input("Hi, type something: ")

#we store it as a string
text = str(text)

#we need to replace every space with "..."
text = text.replace(" ", "...")

#finally, we print the output
print(text)