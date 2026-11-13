#super() lets the child class use the parent's constructor or method.
class Student:
    def __init__(self, name):
        self.name = name


class AIStudent(Student):
    def __init__(self, name, skill):
        super().__init__(name)
        self.skill = skill


student = AIStudent("Sairam", "Machine Learning")

print("Name:", student.name)
print("Skill:", student.skill)

#super().__init__(name)

#It calls the parent class's constructor.S