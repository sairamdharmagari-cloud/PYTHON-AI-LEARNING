from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

iris  = load_iris()

X= iris.data
y= iris.target


X_train, X_test, y_train, y_test= train_test_split(
    X,y,test_size=0.2,
    random_state=42,
    stratify=y
)

model = make_pipeline(
    StandardScaler(),
    SVC(kernel="linear", C=1)
)

model.fit(X_train,y_train)

y_pred=model.predict(X_test)


accuracy = accuracy_score(y_test,y_pred)

print("Accuracy:",round(accuracy*89,2),"%")

new_flower= [[6.1, 3.7, 1.2, 0.4]]

prediction=model.predict(new_flower)

print("Predicted Flower:",
      iris.target_names[prediction[0]])    