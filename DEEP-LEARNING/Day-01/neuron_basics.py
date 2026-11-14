import numpy as np

# 1. Input values
inputs = np.array([5,9])#We give two input values to our neuron.

# 2. Assign weights
weights = np.array([0.7 ,-0.4])#Each input has a corresponding weight.

# 3. Assign bias
bias = 0.21#Bias is an additional value that allows the neuron to adjust its output

# 4. Calculate weighted sum
z = np.dot(inputs,weights) + bias

# 5. Apply sigmoid activation
output = 1/(1+np.exp(-z))#For z=0.5, the sigmoid output is approximately 0.6225.

# 6. Display results
print("Inputs:",inputs)
print("Weights:", weights)
print("Bias:", bias)
print("Weighted Sum:", z)
print("Neuron Output:", output)

# 7. Make a simple binary prediction
if output >= 0.5:
    print("Prediction: Class 1")
else:
    print("Prediction : Class 0")

#Important: This is a single neuron with manually assigned weights.
#  It is not yet a trained neural network.
#  We'll learn how a neuron learns its weights in the next lessons.