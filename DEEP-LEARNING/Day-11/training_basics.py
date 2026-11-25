import torch
import torch.nn as nn
from torch.utils.data import TensorDataset,DataLoader

X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0]
])

y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
    [11.0]
])

dataset = TensorDataset(X,y)

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

# Create NN
model = nn.Sequential(
    nn.Linear(1,8),
    nn.ReLU(),
    nn.Linear(8,1)
)

# Loss fun

loss_function = nn.MSELoss()

# Optimizer
optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

# Training

epochs = 1000

for epoch in range(epochs):

    total_loss =0.0

    for batch_X ,btach_y in loader:

        predictions= model(batch_X)

        # Calc loss
        loss = loss_function(predictions,btach_y)

        # Clear Old Gradients
        optimizer.zero_grad()

        # Backprop
        loss.backward()

        # Update parameters
        optimizer.step()

        total_loss += loss.item()

    average_loss = total_loss / len(loader)

    if ( epoch + 1) % 200 ==0:
        print(
            "Epoch:",epoch + 1,
            "Loss:",round(average_loss,6)
        )

# 8. Test the trained model
model.eval()

with torch.no_grad():

    test_input = torch.tensor([[6.0]])

    prediction = model(test_input)

    print("\nInput:", 6.0)
    print("Predicted Output:", prediction.item())

print("\nTraining completed!")
