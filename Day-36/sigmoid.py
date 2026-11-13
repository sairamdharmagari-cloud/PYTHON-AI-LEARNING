import math

def sigmoid(z):
    return 1/ (1+math.exp(-z))

#Test diff i/p values
values= [-5,-2,0,2,5]

print("\n Sigmoid function results")
print("\n-------------------------")

for value in values:
    result= sigmoid(value)
    print(f"Input:{value:>3} | Output:{result:.4f}")