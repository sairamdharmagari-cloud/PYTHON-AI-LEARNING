from sklearn.preprocessing import StandardScaler

X=[
    [20,20000],
    [30,40000],
    [40,60000],
    [50,80000],
    [60,100000]
]

scaler=StandardScaler()

X_scaled = scaler.fit_transform(X)

print("Original Data:")
print(X)

print("\n Scaled Data:")
print(X_scaled)