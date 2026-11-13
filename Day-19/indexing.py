import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print(numbers[0])
print(numbers[2])
print(numbers[-1])

print(numbers[1:4])

#Just like Python lists, NumPy uses zero-based indexing.


#useful numpy functions
import numpy as np

numbers = np.array([10, 20, 30, 40, 50])

print("Sum:", np.sum(numbers))
print("Mean:", np.mean(numbers))
print("Maximum:", np.max(numbers))
print("Minimum:", np.min(numbers))

#These functions will become very important in data analysis.