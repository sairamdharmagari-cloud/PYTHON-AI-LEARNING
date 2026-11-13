import pandas as pd

from sklearn.preprocessing import StandardScaler

# 1. Create dataset
data = {
    "Name": ["Ravi", "Rahul", "Priya", "Anil", "Sneha"],
    "Study_Hours": [2, 5, 3, 6, 4],
    "Attendance": [60, 90, 75, 95, 80],
    "Marks": [45, 85, 65, 95, 75],
    "City": [
        "Hyderabad",
        "Mumbai",
        "Delhi",
        "Hyderabad",
        "Mumbai"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# 2. Create new feature
df["Study_Efficiency"] = (
    df["Marks"] / df["Study_Hours"]
)

# 3. Create performance category
df["Performance"] = pd.cut(
    df["Marks"],
    bins=[0, 50, 75, 100],
    labels=["Needs Improvement", "Good", "Excellent"],
    include_lowest=True
)

# 4. One-Hot Encode City
df = pd.get_dummies(
    df,
    columns=["City"],
    dtype=int
)

# 5. Encode Performance category
df["Performance_Encoded"] = df["Performance"].cat.codes

# 6. Scale numerical features
features = [
    "Study_Hours",
    "Attendance",
    "Marks",
    "Study_Efficiency"
]

scaler = StandardScaler()

df[features] = scaler.fit_transform(df[features])

print("\nFinal Engineered Dataset:")
print(df)