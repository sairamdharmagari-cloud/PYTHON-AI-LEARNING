import torch
import torch.nn as nn

# TODO 1: Create input data X
X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

# TODO 2: Create output data y
y = torch.tensor([
    [5.0],
    [8.0],
    [11.0],
    [14.0],
    [17.0]
])

# TODO 3: Create a linear model
model = nn.Linear(1,1)

# TODO 4: Create MSE loss function
loss_function = nn.MSELoss()

# TODO 5: Create SGD optimizer
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.02
)

# TODO 6: Train for 1000 epochs
for epoch in range(1000):

    # Forward propagation
    predictions = model(X)

    # Calculate loss
    loss = loss_function(predictions,y)

    # Clear gradients
    optimizer.zero_grad()

    # Backpropagation
    loss.backward()

    # Update parameters
    optimizer.step()

# TODO 7: Predict output for x = 6
test_input = torch.tensor([[6.0]])

prediction = model (test_input)

print("\n Prediction for input 6:")
print(prediction.item())

# TODO 8: Print prediction, learned weight and bias

print("\n Learned Weights:",model.weight.item())
print(" Learned Bias:",model.bias.item())