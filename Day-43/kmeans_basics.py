import numpy as np
from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

X = np.array([
    [1, 2],
    [2, 3],
    [3, 2],
    [8, 8],
    [9, 8],
    [8, 9],
    [15, 2],
    [16, 3],
    [15, 4]
])

#create K-means model
model=KMeans(
    n_clusters=3,
    random_state=42,
    n_init=10# Tries 10 different centroid initializations and retains the best result based on inertia.
)

# Train and assign clusters
labels = model.fit_predict(X)#- fit() learns the clusters.
#- predict() assigns each point to a cluster.
#fit_predict() combines both.


score = silhouette_score(X, labels)
#It measures how well each data point fits into its assigned cluster compared with neighboring clusters.
#The score ranges from -1 to +1.
print("Silhouette Score:", round(score, 3))

# Display cluster labels
print("Cluster Labels:")
print(labels)

#Displat centroids
print("\n Centroids:")
print(model.cluster_centers_) #Shows the center coordinates of each cluster.

#Display inertia
print("\n Inertia:")
print(model.inertia_)#Shows how closely the points are grouped around their centroids.

#Note: Cluster numbers such as 0, 1, and 2 are arbitrary identifiers.
#  They don't represent rankings.

#silhouette score
#Near +1	Good cluster separation
#Near 0	Overlapping clusters
#Near -1	Some points may be assigned to the wrong cluster