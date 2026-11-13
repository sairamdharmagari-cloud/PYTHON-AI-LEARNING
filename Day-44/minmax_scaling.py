import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Original dataset
data= {
    "Age":[20,25,30,35,40],
    "Salary":[20000,30000,40000,50000,60000]
}

df = pd.DataFrame(data)

print(df)

#Create scaler
scaler = MinMaxScaler()

# Scale data
scaled_data = scaler.fit_transform(df)

# Convert back to DataFrame
scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("\n Scaled Data:")
print(scaled_df)