from sklearn.datasets import load_iris

from sklearn.model_selection import(
    GridSearchCV,
    train_test_split
)

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

iris= load_iris()

X=iris.data
y=iris.target

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
)

model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier()
)
# 4. Define hyperparameter grid
param_grid = {
    "kneighborsclassifier__n_neighbors": [3, 5, 7, 9, 11],
    "kneighborsclassifier__weights": ["uniform", "distance"]
}

# 5. Create Grid Search
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=-1
)

# 6. Train and search
grid_search.fit(X_train, y_train)

# 7. Display best parameters
print("Best Parameters:")
print(grid_search.best_params_)

# 8. Display best cross-validation accuracy
print("\nBest CV Accuracy:")
print(grid_search.best_score_)

# 9. Test the best model on unseen test data
best_model = grid_search.best_estimator_

test_accuracy = best_model.score(X_test, y_test)

print("\nTest Accuracy:")
print(test_accuracy)