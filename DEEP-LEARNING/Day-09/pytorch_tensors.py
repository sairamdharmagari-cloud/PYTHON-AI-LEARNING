import torch

a=torch.tensor(5)

b=torch.tensor([1,2,3,])

c=torch.tensor([
    [1,2,4],
    [3,4,6],
    [5,6,9]
])

print("Scalar:", a)
print("Vector:",b)
print("Matrix:",c)

#Check dimensions

print("\nScalar Dimensions:", a.ndim)
print("Vector Dimensions:",b.ndim)
print("Matrix Dimensions:",c.ndim)

# Check Shape
print("\n Matrix Shape:", c.shape)

