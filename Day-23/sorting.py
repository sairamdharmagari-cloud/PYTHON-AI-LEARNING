import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya"],
    "Age": [20, 21, 20, 22, 19],
    "Marks": [90, 65, 82, 95, 55]
}

df = pd.DataFrame(data)

print(df)

#SORT BY MARKS:
sorted_df = df.sort_values("Marks")
print(sorted_df)

#HIGHEST MARKS FIRST:
sorted_df = df.sort_values("Marks", ascending=False)
print(sorted_df)