#Now we will build something more interesting:
#  a perceptron that learns from training examples.

#We'll teach it the AND logic gate.

import numpy as np

# 1. Training data for AND gate
X= np.array([
    [0,0],
    [0,1],
    [1,0],
    [1,1]
])

y = np.array([0,0,0,1])

# 2. Initialize weights and bias
weights = np.zeros(2)
bias = 0.0
#Initially, both weights are zero.
#The perceptron has not learned anything yet.

# 3. Set learning rate and epochs
learning_rate = 0.1 #Controls how much weights and bias change after a mistake.
epochs =10 #An epoch means one complete pass through all training examples.

# 4. Train the perceptron

for epoch in range(epochs):

    total_errors =0
    for inputs ,actual in zip(X,y):
        # Calculate weighted sum
        z = np.dot(inputs,weights)+bias

        # Apply step activation
        prediction = 1 if z >= 0 else 0 #Converts the weighted sum into a binary prediction.

        # Calculate error
        error = actual - prediction

        # Update weights and bias

        weights = weights+ learning_rate * error * inputs
        bias = bias + learning_rate* error

        if error !=0:
            total_errors += 1

    print("Epoch:",epoch +1 ,"Errors:", total_errors)


print("\n Learning Weights:", weights)
print("Learning Bias:", bias)


# 6. Test the trained perceptron

print("\n Final Predictions:")

for inputs in X:

    z= np.dot(inputs ,weights)+bias

    prediction = 1 if z >= 0 else 0

    print(inputs , "->", prediction)#The exact learned weight values depend on the training sequence and initialization.


    
         
#Step 7: Update weights
#weights = weights + learning_rate * error * inputs
#This is the perceptron learning rule.
#If the prediction is correct, error is zero and there is no weight update.
#If the prediction is incorrect, weights and bias are adjusted.