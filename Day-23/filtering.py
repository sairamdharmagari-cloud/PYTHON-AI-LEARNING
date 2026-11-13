# we'll start doing real data analysis with Pandas.
import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya"],
    "Age": [20, 21, 20, 22, 19],
    "Marks": [90, 65, 82, 95, 55]
}

df = pd.DataFrame(data)

print(df)

#filtering
#Suppose we want students whose marks are 80 or above:

high_marks = df[df["Marks"] >= 80]
print(high_marks)

#You can also filter by age:

students_20_plus = df[df["Age"] >= 20]
print(students_20_plus)

#Multiple conditions
#Students who are at least 20 and have marks ≥ 80:

result = df[(df["Age"] >= 20) & (df["Marks"] >= 80)]
print(result)

#With Pandas, use:
#  &

#for AND, and:
#  |

#for OR.