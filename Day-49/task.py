#Now it's your turn. Compare Logistic Regression, KNN, and Random Forest using the Iris dataset.

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
from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import(
    accuracy_score,
    classification_report,
    confusion_matrix
)

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

#2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)



models = {
    "Log Reg":make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
    ),

    "KNN":make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),

    "RF": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}

# TODO 4: Create Stratified K-Fold
cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# TODO 5: Compare models using cross-validation
best_name = None
best_score =-1
best_model = None

for name , model in models.items():

    scores = cross_val_score(
        model,
        X_train,
        y_train,
        cv=cv,
        scoring="accuracy"
    )
    average_score = scores.mean()
    print(name ,"CV Accuracy:", average_score)

   

    # TODO 6: Select the best model
    if average_score > best_score:
        best_score = average_score
        best_name = name
        best_model = model

# TODO 7: Train the best model
best_model.fit(X_train, y_train)

# TODO 8: Make predictions
predictions = best_model.predict(X_test)

# TODO 9: Calculate test accuracy
test_accuracy = accuracy_score(
    y_test,
    predictions
)

# TODO 10: Display final results
print("\nBest Model:", best_name)
print("Best CV Accuracy:", best_score)
print("Final Test Accuracy:", test_accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

print("\nClassification Report:")
print(classification_report(
    y_test,
    predictions,
    target_names=iris.target_names
))





