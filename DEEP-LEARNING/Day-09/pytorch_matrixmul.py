import torch


a = torch.tensor([10,30,50])
b = torch.tensor([1,2,3])

print("Add:",a+b)
print("Sub:",a-b)
print("Mul:",a*b)
print("Div:",a/b)

# Matrix Multiplictaion

x= torch.tensor([
    [1,4],
    [3,1]
])
y = torch.tensor([
    [5,9],
    [7,8]
])

print("\n Martix Multiplication:")
print(torch.matmul(x,y))

#  * performs element-wise multiplication.
# torch.matmul() performs matrix multiplication.