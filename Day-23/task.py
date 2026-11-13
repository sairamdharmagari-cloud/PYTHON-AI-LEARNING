import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya"],
    "Age": [20, 21, 20, 22, 19],
    "Marks": [90, 65, 82, 95, 55]
}

df = pd.DataFrame(data)

# Add result column
df["Passed"] = df["Marks"] >= 35

print("----- All Students -----")
print(df)

print("\n----- Students with Marks >= 80 -----")
print(df[df["Marks"] >= 80])

print("\n----- Sorted by Marks -----")
print(df.sort_values("Marks", ascending=False))

print("\n----- Average Marks -----")
print(df["Marks"].mean())

print("\n----- Highest Marks -----")
print(df["Marks"].max())

best_student = df.loc[df["Marks"].idxmax(), "Name"]
print("\n-----TOP STUDENT------")
print( best_student)