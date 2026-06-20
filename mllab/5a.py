import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
data = pd.read_csv("ToyotaCorolla.csv")
plt.figure(figsize=(8,5))
sns.boxplot(data=data[["Price","HP","KM"]])
plt.title("Box Plot of Toyota Corolla Dataset")
plt.show()