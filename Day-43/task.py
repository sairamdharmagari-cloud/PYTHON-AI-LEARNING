import pandas as pd

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data = {
    "Hours": [
        1, 2, 3, 4, 5,
        6, 7, 8, 9, 10,
        2, 4, 6, 8, 10
    ],

    "Attendance": [
        30, 35, 40, 45, 50,
        60, 65, 70, 80, 90,
        38, 48, 62, 75, 95
    ]
}

df = pd.DataFrame(data)

# 2. Select features
X= df[["Hours","Attendance"]]

# 3. Scale features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 4. Create K-Means model
model = KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10
)

# 5. Train and assign clusters
labels = model.fit_predict(X_scaled)

# 6. Add cluster labels
df["Cluster"]= labels

# 7. Display student groups
print("Student Groups:")
print(df)

# 8. Display cluster centers
print("\nCluster Centers:")
print(model.cluster_centers_)