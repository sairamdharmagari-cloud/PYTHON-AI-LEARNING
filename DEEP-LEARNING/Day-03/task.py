import numpy as np

# TODO 1: Create OR gate training inputs
X = np.array([
    [0, 0],
    [0, 1],
    [1, 0],
    [1, 1]
])

y = np.array([0,1,1,1])

weights = np.zeros(2)

bias = 0.0

learning_rate = 0.1
epochs = 10

for epoch in range(epochs):

    for inputs , actual in zip (X,y):

        z = np.dot(inputs,weights)+bias

        prediction = 1 if z >= 0 else 0

        error = actual - prediction

        weights= weights + learning_rate * error *inputs

        bias = bias + learning_rate * error

print ("\n OR Gate Predictions:")

for inputs in X:

    z= np.dot(inputs, weights)+bias

    prediction = 1 if z>=0 else 0

    print(inputs , "->" , prediction)
