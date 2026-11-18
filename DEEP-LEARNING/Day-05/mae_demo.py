import numpy as np

actual = np.array([10,20,10])

predicted = np.array([90,180,310])

mae = np.mean(np.abs(actual - predicted))

print("MAE:",mae)