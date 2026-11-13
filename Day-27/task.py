import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("../Day26/students.csv")

df["Total"] = (
    df["Physics"]
    + df["Chemistry"]
    + df["Maths"]
)

df["Average"] = df["Total"] / 3

print(df)

#create a student-avg bar chart
plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")

plt.show()

#Create a subject-wise average chart.

#Calculate:

physics_avg = df["Physics"].mean()
chemistry_avg = df["Chemistry"].mean()
maths_avg = df["Maths"].mean()

#Then:

subjects = ["Physics", "Chemistry", "Maths"]
averages = [physics_avg, chemistry_avg, maths_avg]

plt.bar(subjects, averages)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average")

plt.show()

