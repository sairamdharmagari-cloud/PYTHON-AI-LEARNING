import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

# Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 45, 55, 65, 75, 85, 90, 95, 98, 100]
}

df = pd.DataFrame(data)

# Features and target
X = df[["Hours"]]
y = df["Score"]

# Train/Test split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

# Create model
model = LinearRegression()

# Train model
model.fit(X_train, y_train)

# Training R²
train_r2 = model.score(X_train, y_train)

# Testing R²
test_r2 = model.score(X_test, y_test)

print("Training R²:", train_r2)
print("Testing R²:", test_r2)

# Simple interpretation
if train_r2 - test_r2 > 0.2:
    print("Possible overfitting")
else:
    print("No major overfitting detected")