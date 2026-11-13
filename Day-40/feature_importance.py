import pandas as pd
import matplotlib.pyplot as plt
from sklearn.ensemble import RandomForestClassifier

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Attendance": [40, 45, 50, 55, 65, 70, 75, 80, 90, 95],
    "Assignments": [20, 25, 30, 40, 60, 65, 70, 80, 90, 95],
    "Result": [0, 0, 0, 0, 1, 1, 1, 1, 1, 1]
}

df = pd.DataFrame(data)

X = df[["Hours", "Attendance", "Assignments"]]
y = df["Result"]

model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X, y)

importance = model.feature_importances_

for feature, score in zip(X.columns, importance):
    print(feature, ":", round(score, 3))

#visualize
plt.barh(X.columns,importance)
plt.xlabel("Importance")
plt.ylabel("Features")
plt.title("Feature Importance")
plt.show()
#Remember: Feature importance is a model-specific indicator,
#  not proof that a feature causes the outcome.