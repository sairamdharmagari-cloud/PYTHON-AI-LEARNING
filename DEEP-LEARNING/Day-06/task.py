weight = 0.0

learning_rate = 0.1

epochs =15

target = 0.6

for epoch in range(epochs):

    loss = (weight -target)**2

    gradient= 2*(weight-target)

    weight = weight - learning_rate * gradient

    print("Epochs:", epoch+1)
    print("Loss:", round( loss ,6))
    print("Weight:",round(weight,6))

print("\n Final Weight:", round(weight ,6))