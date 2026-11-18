import numpy as np

def softmax(x):
    #Subtract maximum value for numerical stability
    exp_values = np.exp(x)

    # Convert scores into probabilities
    probabilites = exp_values / np.sum(exp_values)

    return probabilites
scores = np.array([4.0,7.0,0.8])

result = softmax(scores)

print("Original Scores:",scores)
print("Softmax Probabilites:",result)
print("Total Probability:",np.sum(result))#np.sum() adds all probabilities.

predicted_class = np.argmax (result)

print("Predicted Class Index:",predicted_class)#np.argmax() returns the index of the highest value.