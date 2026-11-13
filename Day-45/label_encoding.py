import pandas as pd
from sklearn.preprocessing import LabelEncoder

# 1. Create dataset
data={
    "Name": ["Ravi", "Rahul", "Priya", "Anil"],
    "Performance": [
        "Good",
        "Excellent",
        "Average",
        "Good"
    ]
}

df=pd.DataFrame(data)

print(df)

# 2. Create Label Encode
encoder = LabelEncoder()

# 3. Convert text into numbers
df["Performance_Encoded"]=encoder.fit_transform(df["Performance"])

print("\n Encoded Data:")
print(df)

#Dispaly Mapping:

for number,category in enumerate(encoder.classes_):
    print(category, "=", number)