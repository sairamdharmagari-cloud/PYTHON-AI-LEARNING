
#Instead of manually closing the file, Python can handle it automatically:

with open("student_info.txt", "r") as file:
    content = file.read()

print("Student Information")
print(content)

#This is the method I want you to use going forward. 