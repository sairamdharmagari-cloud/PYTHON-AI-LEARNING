import numpy as np

marks = np.array([
    [90, 85, 88],
    [75, 80, 82],
    [95, 92, 90]
])

print("Marks:")
print(marks)

print("Shape:", marks.shape)

print("Total marks:", np.sum(marks))
print("Average:", np.mean(marks))
print("Highest:", np.max(marks))


#AVG MARKS OF EACH STD

import numpy as np

marks = np.array([
    [90, 85, 88],
    [75, 80, 82],
    [95, 92, 90]
])

print("Marks:")
print(marks)

student_averages = np.mean(marks, axis=1)

print("Student averages:", student_averages)

#np.array()       → Create an array
#data[row,column] → Access an element
#.shape            → Rows and columns
#.reshape()        → Change array shape
#axis=1            → Work across rows
#axis=0            → Work down columns