import torch
import torch.nn as nn
from torch.utils.data import TensorDataset , DataLoader , random_split

X = torch.arange(1,101 ,dtype=torch.float32).reshape(-1,1)
y = 2 * X + 1

dataset = TensorDataset(X,y)

total_size = len(dataset)

train_size = int(0.08 * total_size)
validation_size =int(0.12 * total_size)
test_size = total_size - train_size - validation_size

train_dataset , validation_dataset , test_dataset = random_split(
    dataset,
    [train_size,validation_size,test_size]
)

# create dataloaders
train_loader = DataLoader(
    train_dataset,
    batch_size=8,
    shuffle=True
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=8,
    shuffle=True
)

test_loader = DataLoader(
    test_dataset,
    batch_size=8,
    shuffle=True
)

# create model
model = nn.Linear(1,1)

# Loss nd Optimizer
loss_function = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.0001
)

# Trainig
epochs = 10

for epoch in range(epochs):

    model.train()

    total_train_loss = 0.0
    for batch_X ,batch_y in train_loader:

        # forward prop
        predictions = model(batch_X)

        # Clac trainig loss
        loss = loss_function(predictions,batch_y)

        # back prop
        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_loss += loss.item() * len(batch_X)

    avg_train_loss = total_train_loss /len(train_dataset)

    # validation

    model.eval()

    total_validation_loss= 0.0

    with torch.no_grad():

     for batch_X ,batch_y in validation_loader:
    
        # forward prop
        predictions = model(batch_X)
    
        # Clac trainig loss
        loss = loss_function(predictions,batch_y)

        total_validation_loss += loss.item() * len(batch_X)
        
    avg_validation_loss = (
       total_validation_loss /len(validation_dataset)
       )

    # Final testing
    model.eval()

    total_test_loss = 0.0

    with torch.no_grad():

     for batch_X, batch_y in test_loader:

        predictions = model(batch_X)

        loss = loss_function(predictions, batch_y)

        total_test_loss += loss.item() * len(batch_X)

     avg_test_loss = total_test_loss / len(test_dataset)


    if (epoch + 1) % 50 ==0:

       print(
        "Epoch:", epoch + 1,
        " Trainig Loss :", round(avg_train_loss , 4),
        "Validation Loss :" ,round(avg_validation_loss ,4),
        "Fianl Test Loss :" ,round(avg_test_loss,4)
        )

    # Test one new input
    with torch.no_grad():

       test_input = torch.tensor([[101.0]])

       prediction = model(test_input)

       print("Input:", test_input.item())
       print("Predicted Output:", prediction.item())
       print("Expected Output:", 203.0)

    print("\nTraining and evaluation completed!")

       
    




