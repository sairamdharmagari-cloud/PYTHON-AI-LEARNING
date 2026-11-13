import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

subjects = ["Physics", "Chemistry", "Maths"]

averages = [
    df["Physics"].mean(),
    df["Chemistry"].mean(),
    df["Maths"].mean()
]

plt.bar(subjects, averages)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")

plt.show()