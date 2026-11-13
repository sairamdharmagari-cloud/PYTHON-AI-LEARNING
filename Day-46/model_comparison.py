#Let's compare Logistic Regression, KNN, and Decision Tree using the same cross-validation strategy.

from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score ,StratifiedKFold
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Create models

models ={
    "Logistic Regression":make_pipeline(
        StandardScaler(),
        LogisticRegression(max_iter=1000)
    ),

    "KNN": make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),

    "Decision tree":
        DecisionTreeClassifier(
            max_depth=3,
            random_state=42
        )   
}

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# 4. Evaluate each model
for name, model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    print("\nModel:", name)
    print("Fold Scores:", scores)
    print("Average Accuracy:", scores.mean())

