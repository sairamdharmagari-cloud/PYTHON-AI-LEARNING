import numpy as np

values = np.array([-3, -2, -1, 0, 1, 2, 3])
scores = np.array([1.5,2.5,0,5])


def relu(x):
    return np.maximum(0,x)

def sigmoid(x):
    return 1/(1 + np.exp(-x))

def tanh (x):
    return  np.tanh(x)

def step(x):
    return np.where( x >= 0,1,0)

 #Write a Softmax function.
def softmax(x):
    exp_values= np.exp(x)

    probabilites = exp_values / np.sum(exp_values)
    return probabilites

result = softmax(scores)

#: Print the input and all outputs
print("Input Values:", values)

print("ReLU:",relu(values))
print("Sigmoid:",sigmoid(values))
print("Tanh:",tanh(values))
print("Step:",step(values))

# Print the probabilities and their sum.
print("\n Softmax:")
print("Original Scores:",scores)
print("Softmax Prob:",result)
print("Sum of Prabs:",np.sum(result))
