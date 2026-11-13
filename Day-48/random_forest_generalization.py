from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

# 1. Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

models ={
    "Decision Tree": DecisionTreeClassifier(
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        max_depth=5,
        random_state=42
    )
}

for name , model in models.items():

    model.fit(X_train,y_train)

    train_accuracy = accuracy_score(
        y_train,
        model.predict(X_train)
    )

    test_accuracy =accuracy_score(
        y_test,
        model.predict(X_test)
    )

    print("\nModels:",name)
    print("Training Accuracy:",train_accuracy)
    print("Testing Accuracy:",test_accuracy)
