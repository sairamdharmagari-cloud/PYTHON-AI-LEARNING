import torch

# Create a tensor that tracks gradients
x = torch.tensor(3.0,requires_grad=True)

# Mathematical equation
y = x**2 + 2*x + 1

print("Values of y:",y.item())

# Calc gradient
y.backward()

# Display Gradient
print("Gradient:", x.grad.item())

