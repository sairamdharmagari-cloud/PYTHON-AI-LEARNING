import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [40, 45, 50, 55, 65, 70, 75, 80, 90, 95],
    "Assignments": [20, 25, 30, 40, 60, 65, 70, 80, 90, 95],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]

X_train,X_test,y_train,y_test=train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model= RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X_train,y_train)

y_pred= model.predict(X_test)

accuracy=accuracy_score(y_test,y_pred)

print("Accuracy:",round(accuracy*100,2),"%")

prediction=model.predict(pd.DataFrame([[6,76,70]],columns=["Hours","Attendance","Assignments"]))

if prediction[0]==1:
    print("Prediction: Pass")
else:
    print("Prediction: Fail")
