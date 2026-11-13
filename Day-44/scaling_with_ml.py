#Let's combine feature scaling with KNN classification.
from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score

iris = load_iris()

X= iris.data
y = iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

model.fit(X_train,y_train)

y_pred=model.predict(X_test)

accuracy = accuracy_score(y_test,y_pred)

print("Accuracy:",round(accuracy*100,2),"%")

new_flower=[[5.1, 3.5, 1.4, 0.2]]

prediction=model.predict(new_flower)

print(
    "Predicted Flower:",
    iris.target_names[prediction[0]]
)

