import pandas as pd
from sklearn.neighbors import KNeighborsClassifier

data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Result":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)
print(df)

X=df[["Hours"]]
y=df["Result"]

model = KNeighborsClassifier(n_neighbors=3)

model.fit(X,y)

new_student=pd.DataFrame({"Hours": [7]})

prediction= model.predict(new_student)

if prediction[0]==1:
    print("\nPrediction Pass")
else:
    print("\nPrediction Fail")

