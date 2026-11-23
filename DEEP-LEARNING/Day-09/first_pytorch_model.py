import torch 
import torch.nn as nn

X = torch.tensor([
    [1.0],[2.0],[3.0],[4.0],[5.0]
])

y = torch.tensor([
    [3.0], [5.0], [7.0], [9.0], [11.0]
])

# Create a simple neural network
model = nn.Linear(1,1)

# Loss function

loss_function = nn.MSELoss()

# Optimizer

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

# Training
epochs = 1000

for epoch in range(epochs):

    # Forward prop
    predictions = model(X)

    # Calculate loss
    loss = loss_function(predictions ,y)

    # Clear previous gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update weights and bias
    optimizer.step()

    if (epoch +1) % 200 ==0:
        print(
            "Epoch:",epoch +1,
            "Loss:",round(loss.item(),6)
        )

# Test the trained model
test_input = torch.tensor([[0.6]])

prediction =  model(test_input)

print("\n Prediction for input 6:")
print(prediction.item())

# Display learned parameters
print("\n Learned Weight:", model.weight.item())
print("Learned Bias:",model.bias.item())