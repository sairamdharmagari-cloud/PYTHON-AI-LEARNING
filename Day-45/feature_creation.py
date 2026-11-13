#We will create a new feature called BMI using height and weight.

import pandas as pd

data={
    "Name":["Sai","Ram","Ravi"],
    "Weight":[70,80,55],
    "Height":[1.75,1.80,1.60]
}

df=pd.DataFrame(data)

print(df)

#  Create a new feature
df["BMI"]=df["Weight"]/(df["Height"]**2)

#  Display new dataset
print("\nData After Feature Creation:")
print(df)

