from sklearn.datasets import load_iris
from sklearn.model_selection import StratifiedKFold,cross_val_score
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler

from sklearn.linear_model import LogisticRegression
from sklearn.neighbors import KNeighborsClassifier
from sklearn.tree import DecisionTreeClassifier
from sklearn.ensemble import RandomForestClassifier

iris = load_iris()

X= iris.data
y=iris.target

models = {
    "Logistic Regrression": make_pipeline(
        StandardScaler(),
        LogisticRegression()
    ),

    "KNN":make_pipeline(
        StandardScaler(),
        KNeighborsClassifier(n_neighbors=5)
    ),

    "D T": DecisionTreeClassifier(
        max_depth=5,
        random_state=42
    ),

    "RF": RandomForestClassifier(
        n_estimators=100,
        random_state=42
    )
}
#Cross val 
cv = StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

#Compare models
results = {}

for name,model in models.items():

    scores = cross_val_score(
        model,
        X,y,
        cv=cv,
        scoring="accuracy"
    )

    results[name]= scores.mean()#Stores the average accuracy for each algorithm.

    print("\n Models:",name)
    print("Fold Scores:",scores)
    print("Avg Accuracy:",scores.mean())

    #Find best model

    best_model = max(results, key=results.get)#Finds the model with the highest average accuracy

    print("\n Best Model:",best_model)
    print("Best Accuracy:",results[best_model])