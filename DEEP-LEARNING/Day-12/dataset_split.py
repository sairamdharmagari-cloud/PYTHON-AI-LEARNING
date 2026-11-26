import torch
from torch.utils.data import TensorDataset ,random_split

# Make the split reproducible
torch.manual_seed(42)

# Create 100 samples
X = torch.arange(1,101,dtype=torch.float32).reshape(-1,1)

y= 2 * X + 1

# Combine inputs and targets
dataset = TensorDataset(X,y)

# Calculate split sizes
total_size = len(dataset)

train_size = int(0.70 * total_size)
validation_size = int(0.15 * total_size)

test_size = total_size - train_size - validation_size

# Split the dataset
train_dataset ,validation_dataset , test_dataset = random_split(
    dataset,
    [train_size,validation_size,test_size]
)

print("Total Samples :",total_size)
print("Training Samples:",len(train_dataset))
print("Validation Samples:",len(validation_dataset))
print("Testing Samoles:",len(test_dataset))