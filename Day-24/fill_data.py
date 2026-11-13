import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran"],
    "Age": [20, None, 21, 22],
    "Marks": [90, 85, None, 95]
}

df = pd.DataFrame(data)

df["Age"] = df["Age"].fillna(df["Age"].mean())
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

print(df)

#Here we're replacing missing values with the column average.