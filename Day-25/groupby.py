"""we'll learn how to summarize data, which is a major part of data analysis."""

import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya", "Ravi"],
    "Branch": ["AIML", "CSE", "AIML", "CSE", "AIML", "CSE"],
    "Marks": [90, 85, 78, 95, 88, 75]
}

df = pd.DataFrame(data)

print(df)

branch_average = df.groupby("Branch")["Marks"].mean()

print(branch_average)

'''groupby("Branch") groups students according to their branch.

Then:
["Marks"].mean()

calculates the average marks for each group.'''