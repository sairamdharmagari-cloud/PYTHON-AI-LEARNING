import numpy as np

actual = np.array([50,60,70,80])
predicted = np.array([45,65,67,76])

errors = actual - predicted

squared_errors = errors ** 2

mse = np.mean(actual - predicted)

mae = np.mean(np.abs(actual - predicted))

print("Actual:", actual)
print("Predicted:",predicted)
print("Errors:",errors)
print("Squared Errors:",squared_errors)
print("MSE:",mse)
print("MAE:", mae)

# BONUS: Binary Cross-Entropy

labels = np.array([1, 0, 1, 0])
probabilities = np.array([0.85, 0.25, 0.75, 0.10])

epsilon = 1e-4
predicted = np.clip(predicted ,epsilon , 1- epsilon)

bce = -np.mean(
    actual * np.log(predicted)
    +(1 - actual) * np.log(1 - predicted)
)

print("BCE:",bce)