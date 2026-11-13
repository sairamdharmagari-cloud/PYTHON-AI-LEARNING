#We'll use SelectKBest and f_classif to select the
#  three most useful features for a classification task.

import pandas as pd

from sklearn.datasets import load_breast_cancer
from sklearn.feature_selection import SelectKBest,f_classif

# 1.Load dataset

dataset =load_breast_cancer()

X=pd.DataFrame(
    dataset.data,
    columns=dataset.feature_names
)

y= dataset.target

print("Original Feature:")
print(X.shape)


# 2. Create feature selector
seletor =SelectKBest(
    score_func=f_classif,
    k=3
)
# 3. Select important features

X_selected = seletor.fit_transform(X,y)

# 4. Get selected feature names

selected_features = X.columns[
    seletor.get_support()
]

print("\nSelected Features:")
print(selected_features.tolist())

print("\nNew Feature Shape:")
print(X_selected.shape)