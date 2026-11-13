import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran"],
    "Physics": [90, 85, 78, 92],
    "Chemistry": [85, 88, 75, 90],
    "Maths": [95, 82, 80, 88]
}

df = pd.DataFrame(data)

df["Total"] = (
    df["Physics"]
    + df["Chemistry"]
    + df["Maths"]
)

df["Average"] = df["Total"] / 3

#Find the student with the highest average:
best_student = df.loc[df["Average"].idxmax()]

print("Best Student:")
print(best_student)

print(df)

#Pandas
  #↓
#Series     → One column
#DataFrame  → Complete table
#read_csv() → Read CSV data
#head()     → First rows
#info()     → Data information
#describe() → Statistics