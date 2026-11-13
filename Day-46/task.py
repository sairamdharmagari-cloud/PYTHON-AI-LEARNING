from sklearn.datasets import load_iris

from sklearn.model_selection import (
    StratifiedKFold,
    cross_val_score
)

from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# TODO 1: Create StratifiedKFold
# Use 5 splits, shuffle=True, random_state=42

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

#  2: Create Logistic Regression Pipeline
# Use StandardScaler and LogisticRegression(max_iter=1000)

logistic_model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=1000)
)

# 3: Calculate cross-validation accuracy
# Use cross_val_score()

logistic_scores = cross_val_score(
    logistic_model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

# 4: Print individual fold scores
print("\nLogistic Regression Fold Scores:")
print(logistic_scores)


#  5: Print average accuracy
print("\nAvg Accuracy:")
print(logistic_scores.mean())


#  6: Create KNN Pipeline
# Use StandardScaler and KNeighborsClassifier(n_neighbors=5)
knn_model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

#  7: Calculate KNN cross-validation accuracy
knn_scores = cross_val_score(
    knn_model,
    X,
    y,
    cv=cv,
    scoring="accuracy"
)

print("\nKNN Fold Scores:")
print(knn_scores)

print("\nKNN Average Accuracy:")
print(knn_scores.mean())

# 8: Compare the average accuracy of both models
logistic_accuracy = logistic_scores.mean()
knn_accuracy = knn_scores.mean()

print("\nModel Comparison:")

print("Logistic Regression:", logistic_accuracy)
print("KNN:", knn_accuracy)

if logistic_accuracy > knn_accuracy:
    print("Logistic Regression performs better.")

elif knn_accuracy > logistic_accuracy:
    print("KNN performs better.")

else:
    print("Both models have equal accuracy.")