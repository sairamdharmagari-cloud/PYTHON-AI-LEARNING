import pandas as pd
from sklearn.preprocessing import StandardScaler

data = {
    "Age": [20, 25, 30, 35, 40],
    "Salary": [20000, 30000, 40000, 50000, 60000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Create scaler
scaler = StandardScaler()

# Scale data
scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)


print("\nStandardized Data:")
print(scaled_df)

print("\nMeans:")
print(scaler.mean_)

print("\nStandard Deviations:")
print(scaler.scale_)

#scaler.mean_	Mean learned for each feature
#scaler.scale_	Standard deviation used for scaling
#fit_transform()	Learns statistics and scales data
#transform()	Scales new data using learned statistics