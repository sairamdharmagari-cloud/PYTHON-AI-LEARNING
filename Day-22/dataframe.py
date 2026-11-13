#A DataFrame is like a table.
import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun"],
    "Age": [20, 21, 20],
    "Marks": [90, 85, 92]
}

df = pd.DataFrame(data)
print(df)

print(df["Name"])
print(df["Marks"])

print("Average:", df["Marks"].mean())
print("Highest:", df["Marks"].max())
print("Lowest:", df["Marks"].min())


