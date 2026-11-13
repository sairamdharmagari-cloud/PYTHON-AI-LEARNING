import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya", "Ravi"],
    "Branch": ["AIML", "CSE", "AIML", "CSE", "AIML", "CSE"],
    "Marks": [90, 85, 78, 95, 88, 75]
}

df = pd.DataFrame(data)

#1. Overall average
print("Overall Average:", df["Marks"].mean())

#2. Branch-wise average
print(df.groupby("Branch")["Marks"].mean())

#3. Highest marks
print("Highest:", df["Marks"].max())

#4. Lowest marks
print("Lowest:", df["Marks"].min())

#5. Top student
top_student = df.loc[df["Marks"].idxmax(), "Name"]
print("Top Student:", top_student)

#6. Number of students in each branch
print(df["Branch"].value_counts())

#----------------------------------------------
'''groupby()       → Group data
mean()          → Average
max()           → Highest
min()           → Lowest
count()         → Count values
agg()           → Multiple calculations
value_counts()  → Count categories'''