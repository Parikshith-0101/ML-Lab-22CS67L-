import matplotlib.pyplot as plt
from sklearn.datasets import load_iris
from sklearn.decomposition import PCA
from sklearn.discriminant_analysis import LinearDiscriminantAnalysis
iris = load_iris()
X = iris.data
y = iris.target
pca = PCA(n_components=2)
X_pca = pca.fit_transform(X)
print("Original Shape:", X.shape)
print("PCA Shape:", X_pca.shape)
plt.figure(figsize=(6,4))
plt.scatter(X_pca[:,0], X_pca[:,1], c=y)
plt.title("PCA")
plt.show()
lda = LinearDiscriminantAnalysis(n_components=2)
X_lda = lda.fit_transform(X, y)
print("LDA Shape:", X_lda.shape)
plt.figure(figsize=(6,4))
plt.scatter(X_lda[:,0], X_lda[:,1], c=y)
plt.title("LDA")
plt.show()