from sklearn.datasets import load_iris
from sklearn.model_selection import LeaveOneOut ,cross_val_score
from sklearn.neighbors import KNeighborsClassifier

iris = load_iris()

# Use only the first 30 records for demonstration

X=iris.data[:30]
y=iris.target[:30]

model = KNeighborsClassifier(n_neighbors=3)

#  Create LOOCV
loo = LeaveOneOut()

scores=cross_val_score(
    model,X,y,
    cv=loo,
    scoring="accuracy"
)

print("Total Validation Rounds:",len(scores))

print("\nLOOCV Accuracy:")
print(scores.mean())