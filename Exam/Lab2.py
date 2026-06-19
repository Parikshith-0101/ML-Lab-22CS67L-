import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.datasets import load_iris
from mpl_toolkits.mplot3d import Axes3D

# Load Iris Dataset
iris = load_iris()

df = pd.DataFrame(
    iris.data,
    columns=iris.feature_names
)

df["species"] = iris.target

print(df.head())

# -----------------------------------
# 1. Scatter Plot
# -----------------------------------

plt.figure(figsize=(6,4))

plt.scatter(
    df["sepal length (cm)"],
    df["sepal width (cm)"]
)

plt.title("Scatter Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()


# -----------------------------------
# 2. Box Plot
# -----------------------------------

plt.figure(figsize=(8,5))

plt.boxplot(df.iloc[:,0:4])

plt.xticks(
    [1,2,3,4],
    ["Sepal Length",
     "Sepal Width",
     "Petal Length",
     "Petal Width"]
)

plt.title("Box Plot")

plt.show()


# -----------------------------------
# 3. Heat Map
# -----------------------------------

plt.figure(figsize=(6,5))

correlation = df.iloc[:,0:4].corr()

plt.imshow(correlation)

plt.colorbar()

plt.xticks(
    range(4),
    ["SL","SW","PL","PW"]
)

plt.yticks(
    range(4),
    ["SL","SW","PL","PW"]
)

plt.title("Heat Map")

plt.show()


# -----------------------------------
# 4. Contour Plot
# -----------------------------------

x = df["sepal length (cm)"]
y = df["sepal width (cm)"]

X, Y = np.meshgrid(
    np.linspace(x.min(), x.max(), 50),
    np.linspace(y.min(), y.max(), 50)
)

Z = X + Y

plt.figure(figsize=(6,5))

plt.contour(X, Y, Z)

plt.title("Contour Plot")
plt.xlabel("Sepal Length")
plt.ylabel("Sepal Width")

plt.show()


# -----------------------------------
# 5. 3D Surface Plot
# -----------------------------------

fig = plt.figure(figsize=(8,6))

ax = fig.add_subplot(
    111,
    projection='3d'
)

x = np.linspace(0, 10, 50)
y = np.linspace(0, 10, 50)

X, Y = np.meshgrid(x, y)

Z = np.sin(X) + np.cos(Y)

ax.plot_surface(X, Y, Z)

ax.set_title("3D Surface Plot")

plt.show()