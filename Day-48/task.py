from sklearn.datasets import load_breast_cancer

from sklearn.model_selection import train_test_split

from sklearn.tree import DecisionTreeClassifier

from sklearn.metrics import accuracy_score

# 1. Load dataset
data = load_breast_cancer()

X = data.data
y = data.target


X_train,X_test ,y_train,y_test = train_test_split(
    X,y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

depths = [1,3,5,None]

for depth in depths:

    model = DecisionTreeClassifier(
        max_depth=4,
        random_state=42
    )

    model.fit(X_train,y_train)

    train_predictions = model.predict(X_train)
    test_predictions =model.predict(X_test)

    train_accuracy = accuracy_score(
        y_train,
        train_predictions
    )

    test_accuracy = accuracy_score(
        y_test,
        test_predictions
    )

    print ("\n Max Depth :",depth)
    print("Training Accuracy:",train_accuracy)
    print("Testing Accuracy:",test_accuracy)

#7
if train_accuracy < 0.75 and test_accuracy < 0.75:
    print("Possible Underfitting")

elif train_accuracy - test_accuracy > 0.10:
    print("Possible Overfitting")

else:
    print("Reasonable Generalization")


#TODO 7   
#These thresholds are just simple practice rules, not universal definitions. 
#Interpret the actual scores and dataset too.
  

