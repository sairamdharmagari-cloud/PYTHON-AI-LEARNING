#2D arrays, which are extremely important because datasets are often represented as rows and columns.

import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data)

#ACESS ROWS & COLS
import numpy as np

data = np.array([
    [10, 20, 30],
    [40, 50, 60],
    [70, 80, 90]
])

print(data[0])
print(data[1])

print(data[0, 1])
print(data[2, 2])