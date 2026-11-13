from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold ,cross_val_score
from sklearn.linear_model import LogisticRegression

iris = load_iris()

X=iris.data
y= iris.target

model = LogisticRegression(max_iter=1000)

skf =StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,
    X,y,
    cv=skf,
    scoring="accuracy"
)


print("Stratified K-Fold Scores:")
print(scores)

print("\nAverage Accuracy:")
print(scores.mean())