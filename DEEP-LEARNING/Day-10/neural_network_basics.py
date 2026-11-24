
import torch
import torch.nn as nn

# Create our neural network
class MyNeuralNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        # Input layer -> Hidden layer
        self.layer1 = nn.Linear(2, 4)

        # Activation function
        self.relu = nn.ReLU()

        # Hidden layer -> Output layer
        self.layer2 = nn.Linear(4, 1)

        # Output activation
        self.sigmoid = nn.Sigmoid()

    # Define forward propagation
    def forward(self, x):

        x = self.layer1(x)
        x = self.relu(x)

        x = self.layer2(x)
        x = self.sigmoid(x)

        return x


# Create model object
model = MyNeuralNetwork()

# Sample input data
input_data = torch.tensor([[2.0, 3.0]])

# Make prediction
output = model(input_data)

print("Input:", input_data)
print("Output:", output)

print("\nModel Architecture:")
print(model)
