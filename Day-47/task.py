from sklearn.datasets import load_iris

from sklearn.model_selection import (
    train_test_split,
    GridSearchCV
)

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

X_train ,X_test ,y_train ,y_test =train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model= make_pipeline(
    StandardScaler(),
    KNeighborsClassifier()
)

param_grid = {
    "kneighborsclassifier__n_neighbors": [3, 5, 7, 9, 11],
    "kneighborsclassifier__weights": ["uniform", "distance"]
}

grid =GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

grid.fit(X,y)

print("Grid Best Parameters:")
print(grid.best_params_)


best_model= grid.best_estimator_

test_accuracy =best_model.score(X_test,y_test)

print("\n Test Accuracy:")
print(grid.best_score_)