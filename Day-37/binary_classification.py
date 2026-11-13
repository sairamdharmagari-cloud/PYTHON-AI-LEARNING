import pandas as pd
from sklearn.linear_model import LogisticRegression

# Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Result": [0, 0, 0, 0, 0, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

# Input and target
X = df[["Hours"]]
y = df["Result"]

# Create model
model = LogisticRegression()

# Train model
model.fit(X, y)

# New student
new_student = pd.DataFrame({"Hours": [7]})

# Prediction
prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

# Display result
if prediction[0] == 1:
    print("Prediction: PASS")
else:
    print("Prediction: FAIL")

print(
    "Pass Probability:",
    round(probability[0][1] * 100, 2),
    "%"
)