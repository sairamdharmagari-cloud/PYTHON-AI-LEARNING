#learn how to deal with missing and incorrect data. This is a very important real-world AI/ML skill because datasets are often messy.
import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran"],
    "Age": [20, None, 21, 22],
    "Marks": [90, 85, None, 95]
}

df = pd.DataFrame(data)

print(df)

print("\nMissing values:")
print(df.isnull())
#to count missing values
print(df.isnull().sum())

#Think of the process as
#Raw Dataset
    # ↓
#Check missing data
 #    ↓
#Handle missing values
#     ↓
#Remove duplicates
#     ↓
#Clean Dataset
#     ↓
#Machine Learning