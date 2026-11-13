#1.Create the Dataset

#We'll create the data directly in Python first:

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

#2. Calculate Total and Average
df["Total"] = (
    df["Physics"]
    + df["Chemistry"]
    + df["Maths"]
)

df["Average"] = df["Total"] / 3

print("\nStudent Performance:")
print(df)

#3. Add Grade 
def get_grade(average):

    if average >= 90:
        return "A"

    elif average >= 75:
        return "B"

    elif average >= 60:
        return "C"

    elif average >= 35:
        return "D"

    else:
        return "F"


df["Grade"] = df["Average"].apply(get_grade)

print("\nGrades:")
print(df[["Name", "Average", "Grade"]])

#4. Find the Top Student 
top_index = df["Average"].idxmax()

print("\n----- TOP STUDENT -----")
print("Name:", df.loc[top_index, "Name"])
print("Average:", round(df.loc[top_index, "Average"], 2))
print("Grade:", df.loc[top_index, "Grade"])

#5. Branch-wise Analysis
branch_average = df.groupby("Branch")["Average"].mean()

print("\n----- BRANCH AVERAGE -----")
print(branch_average)

#6. Find Students Who Scored 80+
high_performers = df[df["Average"] >= 80]

print("\n----- HIGH PERFORMERS -----")
print(high_performers[["Name", "Average", "Grade"]])

#7. NumPy Analysis

#Convert the averages into a NumPy array:

averages = np.array(df["Average"])

print("\n----- NUMPY ANALYSIS -----")
print("Average:", np.mean(averages))
print("Highest:", np.max(averages))
print("Lowest:", np.min(averages))
print("Standard deviation:", np.std(averages))

#8. Create a Graph 📊
plt.bar(df["Name"], df["Average"])

plt.xlabel("Students")
plt.ylabel("Average Marks")
plt.title("Student Performance")

plt.show()