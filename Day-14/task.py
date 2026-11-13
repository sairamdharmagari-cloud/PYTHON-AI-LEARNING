#write
name = input("Enter your name: ")
age = input("Enter your age: ")
course = input("Enter your course: ")

with open("student_info.txt", "w") as file:
    file.write("Student Information\n")
    file.write("Name: " + name + "\n")
    file.write("Age: " + age + "\n")
    file.write("Course: " + course + "\n")

print("Student information saved!")

#read

with open("student_info.txt", "r") as file:
    content=file.read()
print("\nStudent Information")
print(content)