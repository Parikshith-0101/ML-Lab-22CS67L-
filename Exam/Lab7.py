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
df = pd.read_csv("glass.csv")

# Target Column
target = "Type"

# For Fruit Dataset
# df = pd.read_csv("fruits.csv")
# target = "fruit_label"

# Remove ID column if present
if "Id" in df.columns:
    df.drop("Id", axis=1, inplace=True)

# Encode Categorical Columns
for col in df.columns:
    if df[col].dtype == "object":
        encoder = LabelEncoder()
        df[col] = encoder.fit_transform(df[col])

# Features and Target
X = df.drop(target, axis=1)
y = df[target]

# Train-Test Split
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42,
    stratify=y
)

# Feature Scaling
scaler = StandardScaler()

X_train = scaler.fit_transform(X_train)
X_test = scaler.transform(X_test)

# Different K Values
for k in [3, 5, 7]:

    print("\n" + "=" * 40)
    print(f"K = {k}")
    print("=" * 40)

    # Create and Train Model
    model = KNeighborsClassifier(n_neighbors=k)
    model.fit(X_train, y_train)

    # Prediction
    y_pred = model.predict(X_test)

    # Evaluation
    print("Accuracy :", round(accuracy_score(y_test, y_pred), 4))
    print("Precision:", round(
        precision_score(y_test, y_pred,
                        average="weighted",
                        zero_division=0), 4))
    print("Recall   :", round(
        recall_score(y_test, y_pred,
                     average="weighted",
                     zero_division=0), 4))

    print("\nConfusion Matrix:")
    print(confusion_matrix(y_test, y_pred))
