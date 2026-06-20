import pandas as pd
import matplotlib.pyplot as plt
data = pd.read_csv("ToyotaCorolla.csv")
x = data['KM']
y = data['Weight']
z = data['Price']
plt.tricontourf(x, y, z, levels=20, cmap='jet')
plt.colorbar(label='Price')
plt.xlabel('KM')
plt.ylabel('Weight')
plt.title('Contour Plot')
plt.show()