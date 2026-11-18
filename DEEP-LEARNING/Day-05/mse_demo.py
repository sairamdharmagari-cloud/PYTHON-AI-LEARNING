import numpy as np

actual = np.array([100,200,100])

predicted =np.array([90,180,310])

errors = actual -predicted

squared_errors = errors**2

mse = np.mean(squared_errors)

print("Actual Vlaues:", actual)
print("Predicted Values:",predicted)
print("Errors:",errors)
print("Squared Errors:",squared_errors)
print("MSE:",mse)