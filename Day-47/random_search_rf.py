from sklearn.datasets import load_iris

from sklearn.model_selection import (
    RandomizedSearchCV,
    train_test_split
)

from sklearn.ensemble import RandomForestClassifier

from scipy.stats import randint

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

# 3. Create model
model = RandomForestClassifier(random_state=42)

# 4. Define parameter distributions
param_distributions = {
    "n_estimators": randint(50, 201),
    "max_depth": [None, 3, 5, 7, 10],
    "min_samples_split": randint(2, 10)
}

# 5. Create Randomized Search
random_search = RandomizedSearchCV(
    estimator=model,
    param_distributions=param_distributions,
    n_iter=20,
    cv=5,
    scoring="accuracy",
    random_state=42,
    n_jobs=-1
)

# 6. Train and search
random_search.fit(X_train, y_train)

# 7. Display best parameters
print("Best Parameters:")
print(random_search.best_params_)

# 8. Display best CV score
print("\nBest CV Accuracy:")
print(random_search.best_score_)

# 9. Test best model
best_model = random_search.best_estimator_

print("\nTest Accuracy:")
print(best_model.score(X_test, y_test))