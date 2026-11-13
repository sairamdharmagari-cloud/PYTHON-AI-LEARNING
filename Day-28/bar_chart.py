import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

df["Average"] = (
    df["Physics"]
    + df["Chemistry"]
    + df["Maths"]
) / 3

plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Average Marks")

plt.show()