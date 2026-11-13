import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8],
    "Score": [35, 45, 55, 65, 75, 85, 90, 95]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

model = LinearRegression()

model.fit(X, y)

print("Slope:", model.coef_[0])
print("Intercept:", model.intercept_)

prediction = model.predict([[10]])

print("Predicted score:", prediction[0])

predicted_scores = model.predict(X)

plt.scatter(X, y)

plt.plot(X, predicted_scores)

plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Linear Regression")

plt.show()