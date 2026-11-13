import numpy as np

marks = np.array([
    [90, 85, 88],
    [75, 80, 82],
    [95, 92, 90]
])

print("Average of each student:")
print(np.mean(marks, axis=1))

print("Average of each subject:")
print(np.mean(marks, axis=0))

#axis=1
#Calculates across each row → each student's average.

#axis=0
#Calculates down each column → each subject's average.