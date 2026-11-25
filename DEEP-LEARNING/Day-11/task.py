import torch 
import torch.nn as nn
from torch.utils.data import TensorDataset , DataLoader

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

dataset = TensorDataset(X ,y)

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

model = nn.Sequential(
    nn.Linear(1,8),
    nn.ReLU(),
    nn.Linear(8,1)
)

loss_fuction = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

for epoch in range(1000):

    for batch_X ,batch_y in loader:

        predictions = model(batch_X)

        loss = loss_fuction(predictions ,batch_y)

        optimizer.zero_grad()

        loss.backward()

        optimizer.step()

model.eval()

with torch.no_grad():

    test_input = torch.tensor([[7.0]])
    
    prediction = model(test_input)

    print("\n Input:", 7)
    print("Predicted output:", prediction.item())


