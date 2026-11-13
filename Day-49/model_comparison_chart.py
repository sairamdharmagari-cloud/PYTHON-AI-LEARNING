#Let's display classification model accuracy using a bar chart

import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold, cross_val_score

from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

# 1. Load dataset
iris = load_iris()

X = iris.data
y = iris.target

# 2. Create models
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

# 3. Cross-validation
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

results = {}

for name, model in models.items():

    scores = cross_val_score(
        model,
        X,
        y,
        cv=cv,
        scoring="accuracy"
    )

    results[name] = scores.mean()

# 4. Plot comparison
plt.figure(figsize=(10,5))

plt.bar(
    results.keys(),
    results.values()
)

plt.xlabel ("ML Models")
plt.ylabel("Avg Accuracy")
plt.title("Classification Model Comparison")

plt.xticks(rotation=20)
plt.tight_layout()

plt.show()