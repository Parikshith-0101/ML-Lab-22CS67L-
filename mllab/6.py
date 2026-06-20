import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score
data = pd.read_csv("Titanic-Dataset.csv")
X = data[['Pclass', 'Age', 'Fare']]
X = X.fillna(X.median())
y = data['Survived']
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.1, random_state=42)
nb = GaussianNB()
nb.fit(X_train, y_train)
pred = nb.predict(X_test)
print("90-10 Split Accuracy:",
      accuracy_score(y_test, pred))
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.3, random_state=42)
nb = GaussianNB()
nb.fit(X_train, y_train)
pred = nb.predict(X_test)
print("70-30 Split Accuracy:",
      accuracy_score(y_test, pred))