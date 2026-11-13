class Student:
    def __init__(self, name, marks):
        self.name = name
        self.marks = marks

    def display(self):
        print("Name:", self.name)
        print("Marks:", self.marks)

    def result(self):
        if self.marks >= 35:
            print("Pass")
        else:
            print("Fail")


student = Student("Sairam", 85)

student.display()
student.result()