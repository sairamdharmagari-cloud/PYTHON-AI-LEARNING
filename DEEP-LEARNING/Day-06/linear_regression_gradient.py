#So far, we updated one weight. Now let's learn how to update multiple weights.

#yhat=wx+b --We want to learn w and b from training data.

import numpy as np

X= np.array([1,2,3,4,5], dtype=float)
y=np.array([3,5,7,9,11],dtype=float)

weight = 0.0
bias = 0.0

learning_rate = 0.1
epochs = 10

for epoch in range(epochs):
    # Forward propagation
    predictions = weight * X + bias #Uses the current weight and bias to generate predictions.

    #calc errors
    errors = predictions -y #Compares predictions with actual values.

    #Calc MSE loss
    loss = np.mean(errors **2)

    #calc gradients
#These formulas calculate how the MSE changes with respect to the weight and bias.
    dw =(2 / len(X)) *np.sum(errors* X)
    db =(2 / len(X)) *np.sum(errors)

    #update parameters
    #Adjusts both parameters to reduce the loss.
    weight = weight -learning_rate *dw
    bias = bias - learning_rate *db

    if (epoch +1 )% 100 == 0:
        print(
            "Epoch:", epoch + 1,
            "Loss:", round(loss, 4),
            "Weight:", round(weight, 4),
            "Bias:", round(bias, 4)
        )

print("\nFinal Weight:", weight)
print("Final Bias:", bias)

#Test predictions

new_value = 6
prediction = weight *new_value +bias

print("Prediction for input 6:",prediction)

