import numpy as np

values =np.array([-2,-1,0,1,2])#values we want to pass through different activation functions.

def relu(x):
    return np.maximum(0,x)#np.maximum() compares each value with zero and returns the larger one.

def sigmoid (x):
    return 1 / (1 + np.exp(-x))#np.exp() calculates the exponential value.

def tanh(x):
    return np.tanh(x)#NumPy already provides the tanh function.

def step(x):
    return np.where(x >= 0,1,0)#np.where() checks the condition for each array element

print("Input Vlaues:",values)

print("\n ReLU:", relu(values))
print("Sigmoid:",sigmoid(values))
print("Tanh:",tanh(values))
print("Step:",step(values))