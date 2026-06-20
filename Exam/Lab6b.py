import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB
from sklearn.metrics import accuracy_score, f1_score
from sklearn.impute import SimpleImputer
from sklearn.preprocessing import LabelEncoder

# Load Dataset
df = pd.read_csv("Titanic-Dataset.csv")

# Select Required Columns
df = df[
    ['Survived',
     'Pclass',
     'Age',
     'SibSp',
     'Parch',
     'Fare',
     'Embarked']
]

# Handle Missing Values
imputer = SimpleImputer(strategy="median")
df[['Age', 'Fare']] = imputer.fit_transform(df[['Age', 'Fare']])

# Encode Embarked
df['Embarked'] = df['Embarked'].fillna(df['Embarked'].mode()[0])

encoder = LabelEncoder()
df['Embarked'] = encoder.fit_transform(df['Embarked'])

# Features and Target
X = df.drop('Survived', axis=1)
y = df['Survived']

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.1, random_state=42)
#Train test split of 70-30
X2_train,X2_test,y2_train,y2_test=train_test_split(X,y,test_size=0.3,random_state=31)

# Train Model
model = GaussianNB()
model.fit(X_train, y_train)

# Prediction
y_pred = model.predict(X_test)

# Evaluation
print("Accuracy :", round(accuracy_score(y_test, y_pred), 2))
print("F1 Score :", round(f1_score(y_test, y_pred), 2))
