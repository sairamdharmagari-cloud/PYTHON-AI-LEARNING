import numpy as np

inputs = np.array([2,5,9])

weights = np.array([0.2,0.6,-0.3])

bias = 0.1

z = np.dot(inputs,weights) + bias

# TODO 5: Apply ReLU activation
output = max(0,z)

print("Weighted sum:",z)
print("Neuron Output:",output)