import numpy as np

x = 4.0
weight = 0.4
bias = 0.2
target = 3.0

learning_rate = 0.5

z =x* weight + bias

prediction = 1 / (1 + np.exp(-z))

loss = (prediction - target)**2

gradient_prediction = 2 * (prediction - target)

sigmoid_derivative = prediction * (1 - prediction)

gradient_z = gradient_prediction * sigmoid_derivative

gradient_weight = gradient_z * x

gradient_bias = gradient_z

# Update weight and bias using Gradient Descent

weight = weight - learning_rate * gradient_weight
bias = bias - learning_rate * gradient_bias

# Print prediction, loss, gradients,
# updated weight and updated bias

print("Prediction:", prediction)
print("Loss:", loss)
print("Gradient Prediction:", gradient_prediction)
print("Sigmoid Derivative:",sigmoid_derivative)
print("Gradient_z:", gradient_z)
print("Gradient Weight:",gradient_weight)
print("Gradient Bias:", gradient_bias)
print("Updated Weight:", weight)
print("Updated Bias:", bias)