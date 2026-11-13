import pandas as pd
import matplotlib.pyplot as plt

from sklearn.tree import DecisionTreeClassifier
from sklearn.tree import plot_tree

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Result"]

model = DecisionTreeClassifier(
    max_depth=3,
    random_state=42
)

model.fit(X, y)

plt.figure(figsize=(8,3))

plot_tree(
    model,
    feature_names=["Hours"],
    class_names=["Fail","Pass"],
    filled=True
)

plt.title("Student Pass/Fail Decision Tree")
plt.show()