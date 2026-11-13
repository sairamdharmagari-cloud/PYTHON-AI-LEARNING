#Predict house prices using Random Forest Regression.
import pandas as pd

from sklearn.ensemble import RandomForestRegressor

data = {
    "Size": [500, 700, 900, 1100, 1300, 1500, 1700, 1900],
    "Bedrooms": [1, 1, 2, 2, 3, 3, 3, 4],
    "Price": [15, 20, 25, 30, 35, 40, 45, 50]
}

df = pd.DataFrame(data)

X = df[["Size", "Bedrooms"]]
y = df["Price"]

model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

prediction = model.predict([[1500, 3]])

print("Predicted House Price:", prediction[0], "Lakhs")

#Note: This is a tiny illustrative dataset. 
# Its predictions are not suitable for real property valuation.