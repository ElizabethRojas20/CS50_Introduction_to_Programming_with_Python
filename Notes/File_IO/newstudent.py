import csv

name = input("What is your name? ")
home = input("Where is your home? ")

with open("newstudent.csv", "a") as file: #a is for append
    writer = csv.DictWriter(file, fieldnames=["name", "home"])
    writer.writerow({"name": name, "home": home})