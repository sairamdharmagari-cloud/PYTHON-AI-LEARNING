import numpy as np

inputs=np.array([3,7])

weights = np.array([0.2,-0.5])

bias = -0.4

# 4. Calculate weighted sum
z = np.dot(inputs,weights)+bias

# 5. Apply step activation function
if z >= 0:
    prediction = 1
else:
    prediction = 0

print("Inputs:", inputs)
print("Weights:",weights)
print("Bias:", bias)

print("Weighted Sum:", z)
print("Prediction:", prediction)