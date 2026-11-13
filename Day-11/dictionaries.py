student = {
    "name": "Sairam",
    "age": 20,
    "course": "AI & ML",
    "cgpa": 8.0
}

print(student)

print(student["name"])
print(student["course"])
print(student["cgpa"])

#Change a Value
student["cgpa"] = 8.5
print(student)

#You can also add a new item:
student["city"] = "Kamareddy"
print(student)