import pandas as pd
import joblib

from sklearn.datasets import load_breast_cancer
from sklearn.model_selection import (
    train_test_split,
    StratifiedKFold,
    GridSearchCV
)
from sklearn.pipeline import make_pipeline
from sklearn.preprocessing import StandardScaler
from sklearn.linear_model import LogisticRegression

from sklearn.metrics import(
    accuracy_score,
    classification_report,
    confusion_matrix
)

cancer = load_breast_cancer()

X =cancer.data
y=cancer.target

# 2. Convert data into DataFrame
df = pd.DataFrame(
    X,columns=cancer.feature_names
)

df["target"]=y

#3.Explore dataset
print("Dataset Shape:",df.shape)

print("\n First 5 Rows:")
print(df.head())

print("\n Target Names:")
print(cancer.target_names)

print("\n Target Counts:")
print(df["target"].value_counts())

X_train ,X_test ,y_train,y_test= train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

model = make_pipeline(
    StandardScaler(),
    LogisticRegression(max_iter=5000)
)

#create hyperpara
param_grid = {
    "logisticregression__C": [0.01, 0.1, 1, 10, 100]
}
#CV
cv=StratifiedKFold(
    n_splits=5,
    shuffle=True,
    random_state=42
)

# Hyperpara tuning
grid_search = GridSearchCV(
    estimator=model,
    param_grid=param_grid,
    cv=cv,
    scoring="accuracy",
    n_jobs=-1
)

#Train and find the best model
grid_search.fit(X_train,y_train)

best_model = grid_search.best_estimator_

print("\nBest Parameters:")
print(grid_search.best_params_)

print("\nBest CV Accuracy:")
print(grid_search.best_score_)

#predictions
predictions = best_model.predict(X_test)

accuracy =accuracy_score(
    y_test,
    predictions
)

print("\n Test Accuracy:")
print(accuracy)

print("\nConfusion Matrix:")
print(confusion_matrix(y_test,predictions))

print("\nClassification Report:")
print(
    classification_report(
        y_test,
        predictions,
        target_names=cancer.target_names
    )
)

# 12. Save trained model
joblib.dump(
    best_model,
    "breast_cancer_model.joblib"
)

print("\n Model saved successfully!!")