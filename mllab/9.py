import numpy as np
import matplotlib.pyplot as plt
from scipy.cluster.hierarchy import linkage, dendrogram
from sklearn.datasets import load_iris
iris = load_iris()
data = iris.data[:20]
n = len(data)
pm = np.zeros((n, n))
for i in range(n):
    for j in range(i+1, n):
        pm[i][j] = np.linalg.norm(data[i] - data[j])
        pm[j][i] = pm[i][j]
print("Proximity Matrix:")
print(np.round(pm, 2))
Z = linkage(data, method='single')
dendrogram(Z)
plt.title("Single Linkage")
plt.show()
Z = linkage(data, method='complete')
dendrogram(Z)
plt.title("Complete Linkage")
plt.show()