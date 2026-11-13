#A tuple is similar to a list, but you cannot change its elements after creating it.
student = ("Sairam", 20, "AI & ML", 8.0)

print(student)
print(student[0])
print(student[2])


#Tuple unpacking
student = ("Sairam", 20, "AI & ML")
name, age, course = student

print("Name:", name)
print("Age:", age)
print("Course:", course)