#Challenge: Email Spam Classification
#Build a model that predicts whether an email is Spam or Not Spam
#  based on the number of suspicious words.

import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import confusion_matrix,ConfusionMatrixDisplay
from sklearn.metrics import(
    accuracy_score,
    precision_score,
    recall_score,
    f1_score
)


data = {
    "SuspiciousWords": [
        0, 1, 2, 3, 4, 5, 6, 7, 8, 9,
        1, 3, 5, 7, 2, 4, 6, 8, 0, 9
    ],
    "Spam": [
        0, 0, 0, 0, 0, 1, 1, 1, 1, 1,
        0, 0, 1, 1, 0, 0, 1, 1, 0, 1
    ]
}

df = pd.DataFrame(data)

print(df)

#  1: Select SuspiciousWords as X
X=df[["SuspiciousWords"]]

#  2: Select Spam as y
y = df["Spam"]

#  3: Split the dataset into train and test

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#  4: Create LogisticRegression model
model = LogisticRegression()

#  5: Train the model
model.fit(X_train, y_train)

#  6: Predict test results
y_pred = model.predict(X_test)

print("\n Actual values: ")
print(y_test.values)

print("\n Predicted values:")
print(y_pred)

# 7: Calculate accuracy
accuracy=accuracy_score(y_test,y_pred)
print("\n Accuracy :",accuracy)

#  8: Display confusion matrix
cm =confusion_matrix(y_test,y_pred)
print("\n Confusion Matrix:")
print(cm)

# 9: Calculate precision, recall and F1-score
precision = precision_score(y_test,y_pred,zero_division=0)
reacall=recall_score(y_test,y_pred,zero_division=0)
f1= f1_score(y_test,y_pred,zero_division=0)

print("\n Precision:",precision)
print("\n Recall:",reacall)
print("\n F1 Score:",f1)