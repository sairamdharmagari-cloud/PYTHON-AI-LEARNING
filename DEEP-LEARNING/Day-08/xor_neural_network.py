import numpy as np

X= np.array([
    [0,0],[0,1],[1,0],[1,1]
],dtype=float)

y = np.array([
    [0],[1],[1],[0]
],dtype=float)

# Make random initialization reproducible
np.random.seed(42)

# Initialize weights and biases
# Input layer (2) -> Hidden layer (4)

W1 = np.random.randn(2,4)
b1 = np.zeros((1,4))

# Hidden layer (4) -> Output layer (1)
W2=np.random.randn(4,1)
b2= np.zeros((1,1))

learning_rate= 1.0
epochs = 20000
N =len(X)

def sigmoid(x):
    return 1 / (1 +np.exp(-x))

for epoch in range(epochs):

    # F  P
    Z1 = np.dot(X, W1)+b1
    A1 = sigmoid(Z1)

    Z2 =np.dot(A1 ,W2)+b2
    A2 = sigmoid(Z2)

    # loss
    loss = np.mean((A2 -y)**2)

    # B P
    # Output layer gradients
    dZ2= (2/N)*(A2-y)* A2 * (1 -A2)

    dW2 = np.dot(A1.T,dZ2)
    db2 = np.sum(dZ2,axis=0,keepdims=True)

    # Hidden layer gradients
    dA1 = np.dot(dZ2,W2.T)
    dZ1=dA1* A1 *(1-A1)

    dW1 = np.dot(X.T,dZ1)
    db1 = np.sum(dZ1,axis=0,keepdims=True)

    # Update weights
    W2-= learning_rate *dW2
    b2-= learning_rate *b2

    W1 -= learning_rate * dW1
    b1 -= learning_rate * db1

    # Display progress
    if (epoch +1 ) % 2000 ==0:
        print(
            "Epoch:", epoch +1,
            "Loss:", round(loss ,6)
        )

    
# 5. TEST THE TRAINED NETWORK

print("\n Final XOR Predictions:")

# Forward pass using the learned parameters
Z1 = np.dot(X, W1) + b1
A1 = sigmoid(Z1)

Z2 = np.dot(A1, W2) + b2
A2 = sigmoid(Z2)

for i in range(len(X)):

    probability = A2[i][0]
    predicted_class = 1 if probability >= 0.5 else 0

    print(
        X[i],
        "Probability:", round(probability ,4),
        "prediction:", predicted_class,
        "Actual:", int(y[i][0])
    )

print("\n Final Loss :" , loss)