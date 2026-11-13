import pandas as pd 
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import StandardScaler

data={
    "Annual_Income":[
        15, 18, 20, 22, 25,
         35, 38, 40, 42, 45,
        60, 65, 68, 70, 75,
        85, 90, 95, 98, 100
    ],

    "Spending_Score": [
        20, 25, 18, 22, 28,
        40, 45, 42, 48, 50,
        60, 65, 62, 70, 68,
        80, 85, 82, 90, 95
    ]
}

df = pd.DataFrame(data)

# 2. Select features
X = df[["Annual_Income", "Spending_Score"]]

 #3. Scale the features
scaler = StandardScaler()

X_scaled = scaler.fit_transform(X)

# 4. Create K-Means model
model = KMeans(
    n_clusters=4,
    random_state=42,
    n_init=10
)

# 5. Train and assign clusters
df["Cluster"] = model.fit_predict(X_scaled)

# 6. Print customer groups
print("Customer Segmentation:")
print(df)

# 7. Get centroid positions
centroids = scaler.inverse_transform( #to convert them back into the original income and spending-score scales for plotting.
    model.cluster_centers_
)

# 8. Visualize clusters
plt.figure(figsize=(7,4))

plt.scatter(
    df["Annual_Income"],
    df["Spending_Score"],
    c=df["Cluster"],
   
)

plt.scatter(
    centroids[:,0],
    centroids[:,1],
    marker="X",
    s=200,
    label="Centroids"
)

plt.xlabel("Annual Income")
plt.ylabel("Spending Score")

plt.title("Coustomer Segmentation using K-Means")

plt.legend()
plt.show()