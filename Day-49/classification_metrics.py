#Now let's understand how to evaluate one classification model in more detail.

from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.ensemble import RandomForestClassifier

from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    f1_score,
    confusion_matrix,
    classification_report
)

# 1. Load dataset
data = load_breast_cancer()

X = data.data
y = data.target

# 2. Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Create model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

# 4. Train model
model.fit(X_train, y_train)

# 5. Predict
predictions = model.predict(X_test)

# 6. Calculate metrics
print("Accuracy:",accuracy_score(y_test,predictions))
print("Precision:",precision_score(y_test,predictions))
print("Recall:", recall_score(y_test, predictions))
print("F1 Score:", f1_score(y_test, predictions))

#7. Confusion matrix
print("\nConfusion Matrix:")
print(confusion_matrix(y_test, predictions))

# 8. Complete classification report
print("\nClassification Report:")
print(classification_report(y_test,predictions,target_names=data.target_names))

#---------------------------------------------------------------------------------------

#Why is this useful?

#Suppose you're building a disease detection model. Missing an actual positive case can be costly.
#In that situation, recall may be especially important. In spam detection, precision may matter more if you want to avoid incorrectly marking legitimate messages as spam.
#The correct metric depends on the real-world problem.