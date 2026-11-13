
import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya"],
    "Age": [20, 21, 20, 22, 19],
    "Marks": [90, 65, 82, 95, 55]
}

df = pd.DataFrame(data)

print(df)

#Add a new column
df["Passed"] = df["Marks"] >= 35
print(df)

#Now each student gets True or False.
#Remove a column:

df = df.drop("Age", axis=1)
print(df)

#Select Specific Columns
print(df["Name"])

#Multiple columns:

print(df[["Name", "Marks"]])