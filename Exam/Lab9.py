import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from scipy.cluster.hierarchy import linkage, dendrogram

# Load Iris Dataset
iris = load_iris()

X = iris.data

# Single Linkage
single_linkage = linkage(X, method='single')

plt.figure(figsize=(8, 5))

dendrogram(single_linkage)

plt.title("Agglomerative Clustering - Single Linkage")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.show()


# Complete Linkage
complete_linkage = linkage(X, method='complete')

plt.figure(figsize=(8, 5))

dendrogram(complete_linkage)

plt.title("Agglomerative Clustering - Complete Linkage")
plt.xlabel("Data Points")
plt.ylabel("Distance")

plt.show()
