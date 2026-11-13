import pandas as pd
from sklearn.linear_model import LogisticRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

print(df)

X= df[["Hours"]]
y=df["Result"]

model=LogisticRegression()

model.fit(X,y)

new_student=pd.DataFrame({"Hours": [7]})

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