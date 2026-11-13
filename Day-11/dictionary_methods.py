student = {
    "name": "Sairam",
    "age": 20,
    "course": "AI & ML"
}

print(student.keys())
print(student.values())
print(student.items())

#Get a value
print(student.get("name"))

#Remove an item
student.pop("age")
print(student)