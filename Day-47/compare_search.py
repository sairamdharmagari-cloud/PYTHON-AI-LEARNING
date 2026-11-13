from sklearn.datasets import load_iris

from sklearn.model_selection import (
    GridSearchCV,
    RandomizedSearchCV
)

from sklearn.pipeline import make_pipeline

from sklearn.preprocessing import StandardScaler

from sklearn.neighbors import KNeighborsClassifier

from scipy.stats import randint

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Create pipeline
model = make_pipeline(
    StandardScaler(),
    KNeighborsClassifier()
)

# 3. Grid Search
param_grid = {
    "kneighborsclassifier__n_neighbors": [3, 5, 7, 9, 11]
}


grid = GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy"
)

grid.fit(X, y)

# 4. Randomized Search
param_distributions = {
    "kneighborsclassifier__n_neighbors": randint(1, 20)
}


random = RandomizedSearchCV(
    model,
    param_distributions,
    n_iter=10,
    cv=5,
    scoring="accuracy",
    random_state=42
)

random.fit(X, y)

# 5. Compare results
print("Grid Search Best Parameters:")
print(grid.best_params_)

print("Grid Search Best Accuracy:")
print(grid.best_score_)

print("\nRandom Search Best Parameters:")
print(random.best_params_)

print("Random Search Best Accuracy:")
print(random.best_score_)