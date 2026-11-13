import pandas as pd 
from sklearn.ensemble import RandomForestClassifier

data={
    "Hours":[1,2,3,4,5,6,7,8,9,10],
    "Result":[0,0,0,0,1,1,1,1,1,1]
}

df = pd.DataFrame(data)

X= df[["Hours"]]
y= df["Result"]

model =RandomForestClassifier(
    n_estimators=100,
    random_state=42
)

model.fit(X,y)

prediction=model.predict(pd.DataFrame(
    [[6]],columns=["Hours"]
))

if prediction[0] ==1:
    print("\nPrediction: Pass")
else:
    print("\n Prediction: Fail")