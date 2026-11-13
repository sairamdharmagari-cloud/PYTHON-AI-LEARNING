#Linear Regression in detail: we'll understand the line y = mx + c, how the model finds the best line, predictions, and how to visualize your first ML model.
#Linear Regression is used to predict a continuous numerical value.

import pandas as pd
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6],
    "Score": [35, 45, 55, 65, 75, 85]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

model = LinearRegression()

model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)
