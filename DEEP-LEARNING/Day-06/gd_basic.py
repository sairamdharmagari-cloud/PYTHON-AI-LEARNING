# Gradient Descent from scratch

# Initial weights
weight= 0.2

#LR
learning_rate = 0.1#This determines how much the weight changes in each iteration

# No of iterations
epochs = 10#We repeat the weight-update process ten times

# Target values
target = 3.0

#Training loop
for epoch in range(epochs):
    # Calc loss
    loss= (weight - target)**2  #This tells us how far our current weight is from the target.
    # Calc Gradient
    gradient = 2*(weight -target) #This is the derivative of our loss function.
    # Update weight
    weight = weight -learning_rate * gradient

    print(
        "Epoch:" , epoch +1,
        "Loss:", round(loss ,3),
        "Weight:",round(weight ,3)
    )

print("\n Final Weight :",round(weight ,3))