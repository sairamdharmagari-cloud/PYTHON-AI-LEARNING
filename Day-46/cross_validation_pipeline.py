from sklearn.datasets import load_iris
from sklearn.model_selection import cross_val_score,StratifiedKFold
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

X=iris.data
y=iris.target

model =make_pipeline(
    StandardScaler(),
    KNeighborsClassifier(n_neighbors=5)
)

cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

scores = cross_val_score(
    model,X , y,
    cv=cv,
    scoring="accuracy"

)

print("\n Flod Scores:")
print(scores)

print("\n Avg Accuracy:")
print(scores.mean())

print("\n Std Dev:")
print(scores.std())