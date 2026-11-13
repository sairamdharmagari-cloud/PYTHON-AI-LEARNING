import matplotlib.pyplot as plt

from sklearn.datasets import make_blobs
from sklearn.cluster import KMeans

X,y=make_blobs(  #make_blobs()--Generates sample clustered data
    n_samples=300,
    centers=4, #--Generates four underlying groups
    cluster_std=1.0,
    random_state=42
)

# Store inertia values
inertia_values =[]

# Test different K values
for k in range(1,11):  #Tests K from 1 to 10

    model = KMeans(
        n_clusters=k,
        random_state=42,
        n_init=10
    )

    model.fit(X)

    inertia_values.append(model.inertia_)
    #inertia_values.append()--Stores each inertia result



# Plot elbow graph

plt.plot(
    range(1,11),
    inertia_values,
    marker="o"
)


plt.xlabel("Num of Clusters(K)")
plt.ylabel("Inertia")
plt.title("Elbow Method")
plt.show()