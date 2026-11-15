import numpy as np

inputs = np.array ([3,8])

weights = np.array([0.2,0.6])

bias= 0.3

weighted_inputs = inputs*weights

print("Inputs:",inputs)
print("Weights:",weights)
print("Weighted Inputs:",weighted_inputs)

# 5. Calculate weighted sum and add bias

z= np.sum(weighted_inputs)+bias

print("\n Weighted Sum:", z)

# 6. Apply ReLU activation
output = np.maximum(0,z)
print("Neuron Output:",output)

#Applies ReLU activation.
#Negative values become zero; positive values remain unchanged
