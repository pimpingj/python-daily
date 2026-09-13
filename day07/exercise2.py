def update_student(students, name, age, city):
    students[name] = {"age": age, "city": city}

student1 = {}

update_student(student1, "mia", 23, "Munich")
print(student1)
update_student(student1, "alex", 25, "Berlin")
print(student1)
update_student(student1, "mia", 13, "Exess")
print(student1)