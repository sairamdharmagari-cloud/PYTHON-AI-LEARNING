class Student:
    def __init__(self, name, physics, chemistry, maths):
        self.name = name
        self.physics = physics
        self.chemistry = chemistry
        self.maths = maths

    def total(self):
        return self.physics + self.chemistry + self.maths

    def average(self):
        return self.total() / 3

    def grade(self):
        avg = self.average()

        if avg >= 90:
            return "A"
        elif avg >= 75:
            return "B"
        elif avg >= 60:
            return "C"
        elif avg >= 35:
            return "D"
        else:
            return "Fail"


student = Student("Sairam", 90, 85, 95)

print("Name:", student.name)
print("Total:", student.total())
print("Average:", student.average())
print("Grade:", student.grade())

#Class       → Blueprint
#Object      → Instance of a class
#__init__()  → Constructor
#self        → Current object
#Method      → Function inside a class