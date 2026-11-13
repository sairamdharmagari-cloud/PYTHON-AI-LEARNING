#NumPy can find values based on conditions
import numpy as np

marks = np.array([90, 55, 78, 92, 35, 88, 45])

passed = marks >= 40

print(passed)

#You can also find high marks:

print(marks[marks >= 80])

#This is called Boolean filtering.