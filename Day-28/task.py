#Start with:

import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["Average"] = (
    df["Physics"]
    + df["Chemistry"]
    + df["Maths"]
) / 3

# Find top student
top_index = df["Average"].idxmax()

print("Top Student:", df.loc[top_index, "Name"])
print("Highest Average:", round(df.loc[top_index, "Average"], 2))

#Then create the student chart:

plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average")
plt.title("Student Performance")

plt.show()

#And the subject chart:

subjects = ["Physics", "Chemistry", "Maths"]

averages = [
    df["Physics"].mean(),
    df["Chemistry"].mean(),
    df["Maths"].mean()
]

plt.bar(subjects, averages)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject Performance")

plt.show()

'''Pandas
  ↓
Load / clean / calculate data
  ↓
Matplotlib
  ↓
Visualize the data'''