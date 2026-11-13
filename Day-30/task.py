
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya", "Ravi"],
    "Branch": ["AIML", "CSE", "AIML", "CSE", "AIML", "CSE"],
    "Physics": [90, 75, 78, 95, 88, 65],
    "Chemistry": [85, 80, 75, 90, 92, 70],
    "Maths": [95, 82, 80, 88, 90, 68]
}

df = pd.DataFrame(data)

print(df)


# Q1 - Lowest average

lowest_index = df["Average"].idxmin()

print("\nLowest Student:",
      df.loc[lowest_index, "Name"])

print("Lowest Average:",
      round(df.loc[lowest_index, "Average"], 2))


# Q2 - Students in each branch
print("\nStudents in each branch:")
print(df["Branch"].value_counts())


# Q3 - Average Physics marks
physics_average = df["Physics"].mean()

print("\nAverage Physics Marks:",
      round(physics_average, 2))


# Q4 - Subject average graph
physics_avg = df["Physics"].mean()
chemistry_avg = df["Chemistry"].mean()
maths_avg = df["Maths"].mean()

subjects = ["Physics", "Chemistry", "Maths"]
averages = [physics_avg, chemistry_avg, maths_avg]

plt.bar(subjects, averages)

plt.xlabel("Subjects")
plt.ylabel("Average Marks")
plt.title("Subject-wise Average Marks")

plt.show()


# Q5 - Student ranking
ranking = df.sort_values(
    "Average",
    ascending=False
)

print("\nStudent Ranking:")
print(ranking[["Name", "Average", "Grade"]])