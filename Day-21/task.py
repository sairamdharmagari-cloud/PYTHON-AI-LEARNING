import numpy as np

marks = np.array([
    [90, 85, 88],
    [35, 45, 50],
    [95, 92, 90],
    [60, 70, 65]
])

print("Marks:")
print(marks)

student_average = np.mean(marks, axis=1)

print("Student averages:")
print(student_average)

print("Students with average >= 75:")
print(student_average[student_average >= 75])

print("Highest mark:", np.max(marks))
print("Lowest mark:", np.min(marks))

#Find all marks greater than or equal to 90:
import numpy as np

marks = np.array([
    [90, 85, 88],
    [35, 45, 50],
    [95, 92, 90],
    [60, 70, 65]
])

print("Marks:")
print(marks)

high_marks = marks[marks >= 90]

print("Marks >= 90:", high_marks)

#Make sure you understand:

#np.mean()
#np.median()
#np.max()
#np.min()
#np.std()
#axis=0
#axis=1
#Boolean filtering