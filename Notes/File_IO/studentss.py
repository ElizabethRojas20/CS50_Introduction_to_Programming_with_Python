import csv

studentss = []

with open("studentss.csv") as file:
    reader = csv.reader(file)
    for home, name, house in reader:
        studentss.append({"home": home, "name": name, "house": house})


    #for line in file:
        #name, house = line.rstrip().split(",")
        #student = {"name": name, "house": house}
        #students.append(student)

for student in sorted(studentss, key=lambda student: student["name"]):
    print(f"{student['name']} is in {student['home']}")
