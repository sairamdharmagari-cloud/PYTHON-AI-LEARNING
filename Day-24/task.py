import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Rahul"],
    "Age": [20, None, 21, 22, None],
    "Marks": [90, 85, None, 95, 85]
}

df = pd.DataFrame(data)

print("Original data:")
print(df)

print("\nMissing values:")
print(df.isnull().sum())

# Fill missing ages with average age
df["Age"] = df["Age"].fillna(df["Age"].mean())

# Fill missing marks with average marks
df["Marks"] = df["Marks"].fillna(df["Marks"].mean())

# Remove duplicate rows
df = df.drop_duplicates()

print("\nCleaned data:")
print(df)

#isnull()        → Find missing values
#isnull().sum()  → Count missing values
#fillna()        → Fill missing values
#dropna()        → Remove missing rows
##duplicated()    → Find duplicates
#drop_duplicates() → Remove duplicates