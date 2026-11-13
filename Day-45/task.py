import pandas as pd
from sklearn.preprocessing import LabelEncoder

data = {
    "Name": ["A", "B", "C", "D", "E"],
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000],
    "Department": [
        "IT",
        "HR",
        "IT",
        "Sales",
        "HR"
    ],
    "Performance": [
        "Good",
        "Excellent",
        "Average",
        "Good",
        "Excellent"
    ]
}

df = pd.DataFrame(data)

print("Original Dataset:")
print(df)

# TODO 1: Create a new column Salary_Per_Year
df["Salary_per_year"]=df["Salary"]*12

# TODO 2: Apply One-Hot Encoding to Department
df=pd.get_dummies(df,columns=["Department"],dtype=int)

# TODO 3: Convert Performance into numerical values
encoder=LabelEncoder()
df["Performance_Encoded"]=encoder.fit_transform(df["Performance"])


# TODO 4: Create a new column Age_Group
df["Age_Group"]=df["Age"].apply(
    lambda age:"Young" if age <30 else "Senior"
)
# TODO 5: Display the final engineered dataset
print(df)
