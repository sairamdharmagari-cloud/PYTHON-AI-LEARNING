
import pandas as pd

data = {
    "Name": ["Sairam", "Rahul", "Arjun", "Kiran", "Priya", "Ravi"],
    "Branch": ["AIML", "CSE", "AIML", "CSE", "AIML", "CSE"],
    "Marks": [90, 85, 78, 95, 88, 75]
}

df = pd.DataFrame(data)

result = df.groupby("Branch")["Marks"].agg(
    ["mean", "max", "min", "count"]
)

print(result)