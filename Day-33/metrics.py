from sklearn.metrics import (
    mean_absolute_error,
    mean_squared_error,
    r2_score
)

actual = [50, 60, 70]
predicted = [52, 57, 68]

mae = mean_absolute_error(actual, predicted)

mse = mean_squared_error(actual, predicted)

rmse = mse ** 0.5

r2 = r2_score(actual, predicted)

print("MAE:", mae)
print("MSE:", mse)
print("RMSE:", rmse)
print("R²:", r2)