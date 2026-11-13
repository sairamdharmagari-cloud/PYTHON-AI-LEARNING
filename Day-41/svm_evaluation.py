#We should not judge a model using accuracy alone.
#  Let's also calculate precision, recall, F1-score, and confusion matrix.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.svm import SVC

from sklearn.metrics import(
    accuracy_score,
    confusion_matrix,
    classification_report
)

iris = load_iris()

X = iris.data
y= iris.target

X_train,X_test, y_train ,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
) 

model = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", C=1)
)

model.fit(X_train,y_train)

y_pred = model.predict(X_test)

#Accuracy

print("Accuracy:",accuracy_score(y_test,y_pred))

#confusion matrix

print("Confusion matrix:")
print(confusion_matrix(y_test,y_pred))

#classification report

print("Classification Report:")
print(confusion_matrix(y_test,y_pred))

