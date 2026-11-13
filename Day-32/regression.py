
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

prediction = model.predict([[7]])

print("Predicted score:", prediction[0])
#This is the connection between the math and the Python code.