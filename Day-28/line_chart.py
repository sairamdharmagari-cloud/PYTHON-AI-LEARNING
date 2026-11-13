#we'll combine Pandas + Matplotlib and make a small data-visualization project.
import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("students.csv")

plt.plot(df["Name"], df["Physics"], marker="o", label="Physics")
plt.plot(df["Name"], df["Chemistry"], marker="o", label="Chemistry")
plt.plot(df["Name"], df["Maths"], marker="o", label="Maths")

plt.xlabel("Students")
plt.ylabel("Marks")
plt.title("Subject-wise Marks")

plt.legend()
plt.show()

'''What does marker="o" do?
It puts a small circle at each data point.
And:
plt.legend()
shows which line represents each subject.'''