#we're going to combine everything you've learned in Pandas into one small real-world project.

import pandas as pd

df = pd.read_csv("students.csv")

print("----- STUDENT DATA -----")
print(df)

#CALCULATE TOTAL
df["Total"] = (
    df["Physics"]
    + df["Chemistry"]
    + df["Maths"]
)

print("\n----- TOTAL MARKS -----")
print(df[["Name", "Total"]])

#CALCULATE AVG
df["Average"] = df["Total"] / 3

print("\n----- AVERAGES -----")
print(df[["Name", "Average"]])

#PASS OR FAIL
df["Result"] = (
    (df["Physics"] >= 35) &
    (df["Chemistry"] >= 35) &
    (df["Maths"] >= 35)
)

print("\n----- RESULT -----")
print(df[["Name", "Result"]]) 

#FIND TOP STUDENT
top_student = df.loc[df["Average"].idxmax()]

print("\n----- TOP STUDENT -----")
print("Name:", top_student["Name"])
print("Average:", top_student["Average"])

#BRANCH WISE AVG
branch_average = df.groupby("Branch")["Average"].mean()

print("\n----- BRANCH AVERAGE -----")
print(branch_average)

#SORTING RANKING
sorted_students = df.sort_values(
    "Average",
    ascending=False
)

print("\n----- RANKING -----")
print(sorted_students[["Name", "Branch", "Average"]])