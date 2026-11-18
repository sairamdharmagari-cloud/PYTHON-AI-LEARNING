import numpy as np

actual = np.array([1,0,1,0])
predicted = np.array([0.8,0.4,0.9,0.3])

# Avoid log(0) using clipping
epsilon = 1e-7
predicted = np.clip(predicted ,epsilon, 1 -epsilon)

bce = -np.mean(
    actual * np.log(predicted)
    + (1 - actual) * np.log( 1 - predicted)
)
print("BCE:",bce)
