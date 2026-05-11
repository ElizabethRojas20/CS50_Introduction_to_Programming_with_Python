students = ["Hermione", "Harry", "Ron"]
houses = ["Gryffindor", "Gryffindor", "Gryffindor", "Slytherin"]

print(students[0]) #locate an element in a list
print(students[1])
print(students[2])

for student in students:
    print(student)  #print every element

for i in range(len(students)):
    print(i + 1, students[i])