import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Attendance": [60, 65, 70, 75, 80, 85, 90, 95],
    "PreviousScore": [40, 45, 50, 55, 60, 65, 70, 75],
    "FinalScore": [45, 50, 55, 62, 68, 75, 82, 90]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance", "PreviousScore"]]
y = df["FinalScore"]

model = LinearRegression()

model.fit(X, y)

print("Coefficients:")
print(model.coef_)

print("Intercept:")
print(model.intercept_)