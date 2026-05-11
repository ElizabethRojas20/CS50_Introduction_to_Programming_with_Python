with open("names.txt", "r") as file:
    for line in file: #line is a variable automatically set
    # "rstrip" returns a copy of the string with trailing whitespace removed.
        print("hello,", line.rstrip())