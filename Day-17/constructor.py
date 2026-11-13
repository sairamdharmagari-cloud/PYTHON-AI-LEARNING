class Student:
    def __init__(self, name, age, course):
        self.name = name
        self.age = age
        self.course = course


student1 = Student("Sairam", 20, "AI & ML")
student2 = Student("Rahul", 21, "CSE")

print(student1.name)
print(student1.age)
print(student1.course)

print(student2.name)
print(student2.age)
print(student2.course)