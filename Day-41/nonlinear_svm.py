from sklearn.datasets import make_moons
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.pipeline import make_pipeline
from sklearn.svm import SVC
from sklearn.metrics import accuracy_score

X,y=make_moons(
    n_samples=300,
    noise=0.20,
    random_state=42
)

X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# 3. Create RBF SVM model
model = make_pipeline(
    StandardScaler(),
    SVC(kernel="rbf", C=1, gamma="scale")
)

# 4. Train model
model.fit(X_train, y_train)

# 5. Predict
y_pred = model.predict(X_test)

# 6. Evaluate
accuracy = accuracy_score(y_test, y_pred)

print("RBF SVM Accuracy:", round(accuracy * 100, 2), "%")

# 7. Predict new data
new_data = [[0, 1]]

prediction = model.predict(new_data)

print("Predicted Class:", prediction[0])