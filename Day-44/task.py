import pandas as pd

from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    RobustScaler
)

data = {
    "Hours": [1, 2, 3, 4, 5],
    "Attendance": [30, 40, 50, 60, 100],
    "Marks": [20, 40, 60, 80, 1000]
}

df = pd.DataFrame(data)

print("\nOriginal data:")
print(df)

#  1: Create MinMaxScaler
minmax = MinMaxScaler()
# 2: Apply MinMaxScaler
minmax_data = minmax.fit_transform(df)

standard = StandardScaler()
standard_data = standard.fit_transform(df)

robust = RobustScaler()
robust_data = robust.fit_transform(df)


# 7: Display all three results
print("\n MinMax Scaling:")
print(pd.DataFrame(minmax_data,columns=df.columns))

print("\nStandard Scaling:")
print(pd.DataFrame(standard_data, columns=df.columns))

print("\nRobust Scaling:")
print(pd.DataFrame(robust_data, columns=df.columns))

print("\n Column with extreme value:")
print("Marks column contains an extreme value:1000")