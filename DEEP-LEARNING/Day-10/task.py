import torch
import torch.nn as nn

class MyNetwork(nn.Module):

    def __init__(self):
        super().__init__()

        self.layer1 = nn.Linear(3,8)

        self.relu= nn.ReLU()

        self.layer2 = nn.Linear(8,4)

        self.layer3 = nn.Linear(4,1)

        self.sigmoid = nn.Sigmoid()

    def forward(self,x):

        x= self.layer1(x)
        x= self.relu(x)

        x=self.layer2(x)
        x=self.relu(x)

        x=self.layer3(x)
        x=self.sigmoid(x)

        return x

model = MyNetwork()

input_data = torch.tensor([[1.0, 2.0, 3.0]])

# TODO 11: Get prediction
output = model(input_data)

print("Output:", output)
print("Model Architecture:")
print(model)
