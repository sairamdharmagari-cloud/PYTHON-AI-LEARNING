from sklearn.neighbors import KNeighborsClassifier

# Dataset
X = [
    [1, 2],
    [2, 3],
    [3, 3],
    [6, 7],
    [7, 8],
    [8, 8]
]

# 0 = Class A, 1 = Class B
y = [0, 0, 0, 1, 1, 1]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)

new_point=[[2,4]]

prediction=model.predict(new_point)
print("Prediction:",prediction[0])

if prediction[0]==1:
    print("Class A")
else:
    print("Class B")


#KNeighborsClassifier() creates the KNN model.

#n_neighbors=3 means K = 3.

#fit() trains the model using the dataset.

#predict() predicts the class of new data.