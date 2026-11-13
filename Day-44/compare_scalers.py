#Compare all three scalers

import pandas as pd 

from sklearn.preprocessing import (
    MinMaxScaler,
    StandardScaler,
    RobustScaler
)

data={
     "Salary": [10, 20, 30, 40, 1000],
    "Age": [20, 25, 30, 35, 40]
}

df =pd.DataFrame(data)

minmax= MinMaxScaler()
standard=StandardScaler()
robust=RobustScaler()

minmax_result=minmax.fit_transform(df)
standard_result =standard.fit_transform(df)
robust_result =robust.fit_transform(df)

print("\n Original data:")
print(df)

print("\n MinMax Scaling:")
print(pd.DataFrame(minmax_result,columns=df.columns))

print("\nStandard Scaling:")
print(pd.DataFrame(standard_result, columns=df.columns))

print("\nRobust Scaling:")
print(pd.DataFrame(robust_result, columns=df.columns))