import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#dataset
data={
    "Hours":[1,2,3,4,5],
    "Score":[20,30,45,65,90]
}

df=pd.DataFrame(data)

#i/p o/p features
X=df[["Hours"]]
y=df["Score"]

#create poly reg model
model= make_pipeline(
    PolynomialFeatures(degree=2,include_bias=False),
    LinearRegression()
)

#train the model
model.fit(X,y)

#predict a score of 6 hrs
prediction=model.predict(pd.DataFrame({"Hours":[6]}))

print("Actual dataset:")
print(df)

print("\n Predicted score fpr 6 hrs:",prediction[0])