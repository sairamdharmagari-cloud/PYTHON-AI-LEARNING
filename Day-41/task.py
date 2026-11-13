import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

# Dataset
data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10,
              2, 4, 6, 8, 10],
    "Attendance": [40, 45, 50, 55, 65, 70, 75, 80,
                   90, 95, 48, 58, 72, 85, 98],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1,
               0, 0, 1, 1, 1]
}

df = pd.DataFrame(data)

X= df [["Hours","Attendance"]]
y= df ["Result"]

X_train,X_test, y_train ,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
) 

model = make_pipeline(
    StandardScaler(),
    SVC(kernel="linear", C=1)
)

model.fit(X_train, y_train)

y_pred = model.predict(X_test)

#Accuracy

accuracy = accuracy_score(y_test,y_pred)

print("Accuracy:",round(accuracy*89,2),"%")

prediction=model.predict(pd.DataFrame(
    [[6,85]],columns=["Hours","Attendance"]
))

if prediction[0] ==1:
    print("\nPrediction: Pass")
else:
    print("\n Prediction: Fail")