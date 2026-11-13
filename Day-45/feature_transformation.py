#Sometimes data contains very large values. Log transformation can reduce skewness.
import numpy as np
import pandas as pd 

data={
    "Salary":[
        10000,20000,30000,40000,50000,100000
    ]
}

df = pd.DataFrame(data)
print(df)

# Apply log transformation
df["Log_Salary"] = np.log1p(df["Salary"])

print("\nTransformed Data:")
print(df)

#np.log1p() calculates the natural logarithm of (1 + value). 
# It also handles zero values safely.