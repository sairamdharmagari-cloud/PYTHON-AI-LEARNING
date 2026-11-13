from sklearn.datasets import load_iris
from sklearn.model_selection import GridSearchCV
from sklearn.tree import DecisionTreeClassifier

iris = load_iris()

X=iris.data
y=iris.target

model=DecisionTreeClassifier(random_state=42)

param_grid = {
    "max_depth":[1,3,5,7,None],
    "criterion":["gini", "entropy"],
    "min_samples_split":[2,5,10]
}

grid_search =GridSearchCV(
    model,
    param_grid,
    cv=5,
    scoring="accuracy",
    n_jobs=1
)

grid_search.fit(X , y)

print("Best Parameters:")
print(grid_search.best_params_)

print("\nBest Accuracy:")
print(grid_search.best_score_)