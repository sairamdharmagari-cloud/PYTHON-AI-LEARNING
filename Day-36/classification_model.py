
import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report

# Step 1: Create dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              2, 4, 6, 8, 3, 7, 9, 5, 1, 10],

    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 0, 1, 1, 1, 0, 1]
}

df = pd.DataFrame(data)

# Step 2: Separate inputs and target
X = df[["Hours"]]
y = df["Result"]

# Step 3: Split data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.25,
    random_state=42,
    stratify=y
)

# Step 4: Create and train model
model = LogisticRegression()
model.fit(X_train, y_train)

# Step 5: Predict test results
predictions = model.predict(X_test)

# Step 6: Evaluate model
accuracy = accuracy_score(y_test, predictions)

print("Actual Results:", y_test.tolist())
print("Predicted Results:", predictions.tolist())

print("\nAccuracy:", round(accuracy * 100, 2), "%")

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    zero_division=0
))