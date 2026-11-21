import numpy as np

X = np.array ([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
],dtype=float)

y = np.array ([
    [0],
    [0],
    [0],
    [1]
],dtype=float)

# Make results reproducible

np.random.seed (42)

# Initialize weights and biases

W1=np.random.randn(2,2)*0.5
b1=np.zeros((1,2))

W2=np.random.randn(2,1)*0.5
b2=np.zeros((1,1))

learning_rate = 1.0
epochs =10000
N = len(X)

#Sigmoid Activation fun
def sigmoid(x):
    return 1 /(1 + np.exp(-x))

#Trainig Loop
for epoch in range(epochs):

    #Forward prop
    Z1 = np.dot(X,W1)+ b1
    A1 = sigmoid(Z1)

    Z2 = np.dot(X,W2)+ b2
    A2 = sigmoid(Z2)

    #Calc loss

    loss = np.mean((A2 -y)** 2)

    #Back Prop

    #output layer gradient
    dZ2 = (2/N) * (A2 -y) * A2 *(1-A2)

    dW2 = np.dot(A1.T,dZ2)
    db2 = np.sum(dZ2, axis=0, keepdims=True)

    # Hidden layer gradient
    dA1 = np.dot(dZ2, W2.T)
    dZ1 = dA1 * A1 * (1 - A1)

    dW1 = np.dot(X.T, dZ1)
    db1 = np.sum(dZ1, axis=0, keepdims=True)

    # GRADIENT DESCENT - UPDATE PARAMETERS

    W2 -= learning_rate * dW2
    b2 -= learning_rate * db2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    if (epoch +1 ) % 2000 ==0:
        print("Epoch:",epoch+1 , "Loss:",round(loss,6))


#Final prediction

print("\n Final Prediction:")

for i in range(len(X)):
    print(
        X[i],
        "->",
        round(A2[i][0], 4)
    )

    print("\n Final Loss:", loss)