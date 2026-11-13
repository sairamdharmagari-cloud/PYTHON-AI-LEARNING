import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya", "Ravi"],
    "Branch": ["AIML", "CSE", "AIML", "CSE", "AIML", "CSE"],
    "Marks": [90, 85, 78, 95, 88, 75]
}

df = pd.DataFrame(data)

print("Overall average:", df["Marks"].mean())

print("Highest marks:", df["Marks"].max())

print("Lowest marks:", df["Marks"].min())

top_student = df.loc[df["Marks"].idxmax(), "Name"]

print("Top student:", top_student)

print("\nBranch-wise average:")
print(df.groupby("Branch")["Marks"].mean())