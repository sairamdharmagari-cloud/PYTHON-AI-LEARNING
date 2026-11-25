import torch
from torch.utils.data import Dataset , DataLoader

# Training data
X = torch.tensor([
    [1.0],
    [2.0],
    [3.0],
    [4.0],
    [5.0],
    [6.0]
])

y = torch.tensor([
    [3.0],
    [5.0],
    [7.0],
    [9.0],
    [11.0],
    [13.0]
])

# create custom Dataset
class MyDataset(Dataset):

    def __init__(self,X ,y):
        self.X = X
        self.y = y

    def __len__(self):
        return len(self.X)

    def __getitem__(self, index):
        return self.X [index] , self.y [index]

# Create dataset object
dataset = MyDataset(X,y)

# Create Dataloader

loader = DataLoader(
    dataset,
    batch_size=2,
    shuffle=True
)

# Display batches
for batch_X,batch_y in loader:

    print("Input:")
    print(batch_X)

    print("Actual Output:")
    print(batch_y)

    print("-----------------")
