#Now predict one of three flower species using the famous Iris dataset.

from sklearn.datasets import load_iris
from sklearn.model_selection import train_test_split
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import accuracy_score

#Load dataset

iris = load_iris()

X = iris.data
y = iris.target

#split

X_train , X_test, y_train , y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

#create model
model= LogisticRegression()

#train
model.fit(X_train,y_train)

#Predict
predictions = model.predict(X_test)

#Accuracy

accuracy=accuracy_score(y_test,predictions)

print("Flower Names:",iris.target_names)
print("Actual Classes:",y_test[:10])
print("Predicted Classes:",predictions[:10])
print("Accuracy:",round(accuracy*100,2), "%")

#predict one new flower
new_flower=[X_test[0]]
prediction = model.predict(new_flower)

print("Predicted Flower:",iris.target_names[prediction[0]])

#Here, the three classes are:
#- Setosa
#- Versicolor
#- Virginica
#The Iris dataset is built into Scikit-learn, so you don't need to download a CSV file.