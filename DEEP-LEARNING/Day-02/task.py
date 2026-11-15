import numpy as np 

inputs = np.array([4,7])

weights = np.array([0.2,0.5])

bias = 0.1

weighted_inputs =inputs*weights

z = np.sum(weighted_inputs)+bias

output = np.maximum(0,z)

print("Inputs:",inputs)
print("Weights:",weights)
print("Weighted Inputs:", weighted_inputs )
print("Bias:",bias)
print("Weighted sum:", z)
print("Final Output:",output)