import pandas as pd
from sklearn.linear_model import LogisticRegression

# Step 1: Create a dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print("Student Dataset:")
print(df)

# Step 2: Select input and target
X = df[["Hours"]]
y = df["Result"]

# Step 3: Create the model
model = LogisticRegression()

# Step 4: Train the model
model.fit(X, y)

# Step 5: Predict for a new student
new_student = pd.DataFrame({"Hours": [8]})

prediction = model.predict(new_student)
probability = model.predict_proba(new_student)

if prediction[0] == 1:
    print("\nPrediction: Pass")
else:
    print("\nPrediction: Fail")

print(
    "Probability of passing:",
    round(probability[0][1] * 100, 2),
    "%"
)