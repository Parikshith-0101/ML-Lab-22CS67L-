import pandas as pd

from sklearn.model_selection import train_test_split
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import accuracy_score


def run_knn(dataset_name, file_path, target):

    print("\n" + "="*60)
    print(dataset_name)
    print("="*60)

    # Load Dataset
    df = pd.read_csv(file_path)

    # Remove ID column if present
    if "Id" in df.columns:
        df.drop("Id", axis=1, inplace=True)

    # Encode categorical columns
    for col in df.columns:
        if df[col].dtype == "object":
            encoder = LabelEncoder()
            df[col] = encoder.fit_transform(df[col])

    X = df.drop(target, axis=1)
    y = df[target]

    splits = [0.1, 0.3]
    metrics = ["euclidean", "manhattan"]
    k_values = [3, 5, 7]

    for split in splits:

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=split,
            random_state=42,
            stratify=y
        )

        # Feature Scaling
        scaler = StandardScaler()

        X_train = scaler.fit_transform(X_train)
        X_test = scaler.transform(X_test)

        print(f"\nTrain-Test Split = {int((1-split)*100)}-{int(split*100)}")

        for metric in metrics:

            print(f"\nDistance Metric = {metric}")

            for k in k_values:

                model = KNeighborsClassifier(
                    n_neighbors=k,
                    metric=metric
                )

                model.fit(X_train, y_train)

                y_pred = model.predict(X_test)

                accuracy = accuracy_score(y_test, y_pred)

                print(
                    f"K = {k}  |  Accuracy = {accuracy:.4f}"
                )


# Glass Dataset
run_knn(
    "Glass Dataset",
    "glass.csv",
    "Type"
)

# Fruit Dataset
run_knn(
    "Fruit Dataset",
    "fruits.csv",
    "fruit_label"
)
