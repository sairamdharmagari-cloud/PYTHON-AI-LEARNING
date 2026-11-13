import pandas as pd
from sklearn.preprocessing import RobustScaler

data = {
    "Salary": [10, 20, 30, 40, 1000]
}

df = pd.DataFrame(data)

print("Original Data:")
print(df)

# Create RobustScaler
scaler = RobustScaler()

# Scale data
scaled_data = scaler.fit_transform(df)

scaled_df = pd.DataFrame(
    scaled_data,
    columns=df.columns
)

print("\nRobust Scaled Data:")
print(scaled_df)