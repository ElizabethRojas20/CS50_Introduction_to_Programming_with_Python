name = input("what's your name? ")

#when using open, the second argument is the mode
#it tells python what to do
# "w" means "write mode", used to write new content into a file
#if a file with that name exists, cleans it, if it doesn't it creates it
# "r" means "read mode", used to read the contents of an existing file

#file = open("names.txt", "w") #open file in write mode

# "a" is append, this adds object to the end of the list

#file = open("names.txt", "a")
#file.write(f"{name}\n") #writes the content of variable name into the file

# "\n" is enter
#file.close() #closes the file, saves changes

with open("names.txt", "a") as file: #this opens and closes the file automatically
    file.write(f"{name}\n")
