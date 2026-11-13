
from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    cross_val_score
)

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.ensemble import RandomForestClassifier

# TODO 1: Load the dataset
cancer = load_breast_cancer()

X = cancer.data
y = cancer.target

# TODO 2: Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# TODO 3: Create three models
models = {
    "Logistic Regression": make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=5000)
    ),

    "KNN": make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),

    "Random Forest": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

# TODO 4: Create Stratified K-Fold
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# TODO 5: Compare models
best_name = None
best_score = -1
best_model = None

for name, model in models.items():

    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="accuracy"
    )

    average_score = scores.mean()

    print(name, "Accuracy:", average_score)

    # TODO 6: Select the best model
    if average_score > best_score:
        best_score = average_score
        best_name = name
        best_model = model

# TODO 7: Train the best model
best_model.fit(X_train, y_train)

# TODO 8: Test the best model
test_accuracy = best_model.score(X_test, y_test)

# TODO 9: Display final results
print("\nBest Model:", best_name)
print("Best CV Accuracy:", best_score)
print("Test Accuracy:", test_accuracy)
