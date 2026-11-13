import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.preprocessing import PolynomialFeatures
from sklearn.pipeline import make_pipeline

#dataset
data={
      "Size": [500, 700, 900, 1100, 1300],
    "Price": [20, 28, 40, 58, 80]
}


df=pd.DataFrame(data)

#i/p o/p features
X=df[["Size"]]
y=df["Price"]

#create poly reg model
model= make_pipeline(
    PolynomialFeatures(degree=2),
    LinearRegression()
)

#train the model
model.fit(X,y)

# Predict the price for a house of size 1500
new_house = pd.DataFrame({"Size": [1500]})
predicted_price = model.predict(new_house)

print("Predicted price:", round(predicted_price[0], 2))