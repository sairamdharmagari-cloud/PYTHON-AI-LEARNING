import pandas as pd 
from sklearn.tree import DecisionTreeClassifier

data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Result":[0,0,0,0,1,1,1,1,1,1]
}

df=pd.DataFrame(data)
print(df)

X =df [["Hours"]]
y =df ["Result"]

model=DecisionTreeClassifier(
    criterion="gini",
    max_depth=3,
    random_state=42
)

model.fit(X,y)

prediction=model.predict([[6]])

if prediction[0] ==1:
    print("Students will pass")
else:
    print("Students will fail")