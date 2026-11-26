import torch
import torch.nn as nn
from torch.utils.data import TensorDataset, DataLoader, random_split

torch.manual_seed(42)


X = torch.arange(1, 101, dtype=torch.float32).reshape(-1, 1)

y = 3 * X + 2

dataset = TensorDataset(X ,y)

train_size = int(0.70 * len(dataset))
validation_size = int(0.15 * len(dataset))
test_size = len(dataset) - train_size - validation_size

train_dataset , validation_dataset , test_dataset = random_split(
    dataset,
    [train_size,validation_size,test_size]
)

train_lodaer = DataLoader(
    train_dataset,
    batch_size=8,
    shuffle=True
)

validation_loader = DataLoader(
    validation_dataset,
    batch_size=8,
    shuffle=True
)

test_loader= DataLoader(
    test_dataset,
    batch_size=8,
    shuffle=True
)

model = nn.Linear(1,1)

loss_function = nn.MSELoss()

optimizer = torch.optim.SGD(
    model.parameters(),
    lr=0.01
)

epochs = 20

for epoch in range(epochs):

    model.train()

    total_train_loss =0.0

    for batch_X ,batch_y in train_lodaer:

        predictions = model(batch_X)

        loss = loss_function(predictions , batch_y)

        optimizer.zero_grad()
        loss.backward()
        optimizer.step()

        total_train_loss += loss.item() * len(batch_X)

    avg_train_loss = total_train_loss /len(train_dataset)


    model.eval()

    total_validation_loss = 0.0

    with torch.no_grad():

     for batch_X , batch_y in validation_loader:

        predictions = model(batch_X)

        loss = loss_function(predictions , batch_y)

        total_validation_loss += loss.item() * len(batch_X)

    avg_validation_loss = total_validation_loss / len(validation_dataset)


    model.eval()

    total_test_loss = 0.0

    with torch.no_grad():

       for batch_X , batch_y in test_loader:

          predictions = model(batch_X)

          loss = loss_function(predictions , batch_y)

          total_test_loss += loss.item() * len(batch_X)

    avg_test_loss = total_test_loss / len(test_dataset)


    with torch.no_grad():

       test_input = torch.tensor([[101.0]])

       prediction = model(test_input)

       print("Input:", test_input.item())
       print("Predicted Output:",prediction.item())
       print("Expected Output:",305.0)





