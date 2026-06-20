from sklearn.datasets import load_iris
import matplotlib.pyplot as plt
iris = load_iris()
x = iris.data[:, 0] 
y = iris.data[:, 2]
plt.scatter(x, y, c=iris.target)
plt.xlabel("Sepal Length")
plt.ylabel("Petal Length")
plt.title("Scatter Plot of Iris Dataset")
plt.show()