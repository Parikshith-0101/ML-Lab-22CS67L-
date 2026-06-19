import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)


# Load Dataset
df = pd.read_csv("glass.csv")      # Change file name if needed

# Target Column
target = "Type"                    # Change target column if needed


# df = pd.read_csv("fruits.csv")
# target = "fruit_label"


# Encode Categorical Columns
for col in df.columns:
    if df[col].dtype == "object":
        le = LabelEncoder()
        df[col] = le.fit_transform(df[col])


# Features and Target
X = df.drop(target, axis=1)
y = df[target]



# Feature Scaling
scaler = StandardScaler()
X = scaler.fit_transform(X)


# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)


# Different K Values
k_values = [3, 5, 7]

for k in k_values:

    print("\n" + "=" * 50)
    print(f"K = {k}")
    print("=" * 50)

    # Create Model
    model = KNeighborsClassifier(n_neighbors=k)

    # Train Model
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    accuracy = accuracy_score(y_test, y_pred)

    precision = precision_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    recall = recall_score(
        y_test,
        y_pred,
        average="weighted",
        zero_division=0
    )

    cm = confusion_matrix(y_test, y_pred)

    # Display Results
    print("Accuracy :", round(accuracy, 4))
    print("Precision:", round(precision, 4))
    print("Recall   :", round(recall, 4))

    print("\nConfusion Matrix:")
    print(cm)

