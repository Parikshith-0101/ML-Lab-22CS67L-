from sklearn.model_selection import train_test_split
import pandas as pd
from sklearn.metrics import accuracy_score, f1_score
from sklearn.naive_bayes import GaussianNB

df=pd.read_csv("iris_dataset.csv")
# df.head()
# df.info()
X=df.drop(columns=["target"],axis=1)
# X.head()
y=df["target"]
# y.head()
#Train test split of 90-10
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.1,random_state=42)
#Train test split of 70-30
X_train,X_test,y_train,y_test=train_test_split(X,y,test_size=0.3,random_state=42)
#Training a Gaussian Naive Bayes ML Model
model_gb=GaussianNB()
model_gb.fit(X_train,y_train)
#Test/Prediction
y_pred=model_gb.predict(X_test)
print(f"Accuracy:{ accuracy_score(y_test, y_pred):.2f}")
print(f"F1_Score:{f1_score(y_test, y_pred,average="weighted"):.2f}")