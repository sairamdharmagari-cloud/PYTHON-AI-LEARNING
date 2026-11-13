import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression

data = {
    "Hours": [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    "Score": [35, 45, 55, 65, 75, 85, 90, 95, 98, 100]
}

df = pd.DataFrame(data)

X = df[["Hours"]]
y = df["Score"]

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

model = LinearRegression()

model.fit(X_train, y_train)

prediction = model.predict([[11]])


print("Predicted score:", prediction[0])

'''
X              → Features/input
y              → Target/output

Training data  → Model learns from it
Testing data   → Evaluate on unseen data

Regression     → Predict numbers
Classification → Predict categories
Clustering     → Find groups

fit()          → Train the model
predict()      → Make predictions
'''

'''One thing I especially want you to understand

Don't worry about memorizing the Scikit-learn code yet.

For now, understand this:

"What information do I have?"
             ↓
          X = input
             ↓
"What am I trying to predict?"
             ↓
          y = target
             ↓
       Train the model
             ↓S
       Give new X
             ↓
       Get prediction

That's the heart of supervised machine learning.
'''