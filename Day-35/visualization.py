import pandas as pd
import matplotlib.pyplot as plt

from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Score": [20, 30, 45, 65, 90]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

model = make_pipeline(
    PolynomialFeatures(degree=2, include_bias=False),
    LinearRegression()
)

model.fit(X, y)

# Generate points for a smooth curve
curve_hours = pd.DataFrame({
    "Hours": [i / 10 for i in range(10, 61)]
})

curve_scores = model.predict(curve_hours)

# Plot actual data and predictions
plt.scatter(X["Hours"], y, label="Actual Scores")
plt.plot(
    curve_hours["Hours"],
    curve_scores,
    label="Polynomial Curve"
)

plt.xlabel("Hours Studied")
plt.ylabel("Score")
plt.title("Polynomial Regression")
plt.legend()
plt.grid(True)
plt.show()