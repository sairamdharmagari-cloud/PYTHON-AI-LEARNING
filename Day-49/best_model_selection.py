#Let's combine cross validation, model comparison, and final test evaluation.

from sklearn.datasets import load_iris

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score
)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import accuracy_score

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Create models
models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
    ),

    "KNN": make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),

    "Decision Tree": DecisionTreeClassifier(
        max_depth=3,
        random_state=42
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

# 4. Create cross validation
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# 5. Find the best model using training data

best_name = None
best_score = -1
best_model =None

for name,model in models.items():
    scores=cross_val_score(
        model,
        X_train,y_train,
        cv=cv,
        scoring="accuracy"
    )

    average_score= scores.mean()

    print(name , "CV Accuracy:",average_score)

    if average_score> best_score:
        best_score = average_score
        best_name = name
        best_model= model

# 6. Train selected model
best_model.fit(X_train, y_train)

# 7. Test on unseen data
predictions = best_model.predict(X_test)

test_accuracy = accuracy_score(
    y_test,
    predictions
)

# 8. Display final results
print("\nBest Model:", best_name)
print("Best CV Accuracy:", best_score)
print("Final Test Accuracy:", test_accuracy)