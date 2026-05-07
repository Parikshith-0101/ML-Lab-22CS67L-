import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.neighbors import KNeighborsClassifier
from sklearn.metrics import (
    accuracy_score,
    precision_score,
    recall_score,
    confusion_matrix
)


# Function for KNN

def run_knn(dataset_name, file_path, target_column):

    print("\n" + "="*70)
    print(f"{dataset_name}")
    print("="*70)

    # Load dataset
    df = pd.read_csv(file_path)

    print("\nFirst 5 Rows:")
    print(df.head())

    X = df.drop(target_column, axis=1)
    y = df[target_column]

    # Different train-test splits
    splits = [0.1, 0.3]

    # Different K values
    k_values = [3, 5, 7]

    # Distance metrics
    metrics = ['euclidean', 'manhattan']

    accuracy_list = []
    precision_list = []
    recall_list = []
    labels = []

    
    # Run all combinations
    
    for split in splits:

        X_train, X_test, y_train, y_test = train_test_split(
            X,
            y,
            test_size=split,
            random_state=42
        )

        print("\n" + "-"*50)
        print(f"Train-Test Split = {int((1-split)*100)}-{int(split*100)}")
        print("-"*50)

        for metric in metrics:

            print(f"\nDistance Metric: {metric.upper()}")

            for k in k_values:

                # Create model
                model = KNeighborsClassifier(
                    n_neighbors=k,
                    metric=metric
                )

                # Train model
                model.fit(X_train, y_train)

                # Prediction
                y_pred = model.predict(X_test)

                # Evaluation Metrics
                accuracy = accuracy_score(y_test, y_pred)

                precision = precision_score(
                    y_test,
                    y_pred,
                    average='weighted',
                    zero_division=0
                )

                recall = recall_score(
                    y_test,
                    y_pred,
                    average='weighted',
                    zero_division=0
                )

                # Store results
                accuracy_list.append(accuracy)
                precision_list.append(precision)
                recall_list.append(recall)

                labels.append(
                    f"K={k}\n{metric[:4]}\n{int((1-split)*100)}-{int(split*100)}"
                )

                # Print Results
                print(f"\nK = {k}")
                print(f"Accuracy  : {accuracy:.4f}")
                print(f"Precision : {precision:.4f}")
                print(f"Recall    : {recall:.4f}")

                # Confusion Matrix
                cm = confusion_matrix(y_test, y_pred)

                print("Confusion Matrix:")
                print(cm)

    
    # Visualization
    
    plt.figure(figsize=(14, 6))

    plt.plot(labels, accuracy_list, marker='o', label='Accuracy')
    plt.plot(labels, precision_list, marker='s', label='Precision')
    plt.plot(labels, recall_list, marker='^', label='Recall')

    plt.title(f"KNN Performance Metrics - {dataset_name}")
    plt.xlabel("K Value | Distance Metric | Train-Test Split")
    plt.ylabel("Score")

    plt.legend()
    plt.grid(True)

    plt.show()



# Glass Dataset

run_knn(
    dataset_name="Glass Dataset",
    file_path="glass.csv",
    target_column="Type"
)


# Fruit Dataset

run_knn(
    dataset_name="Fruit Dataset",
    file_path="fruit.csv",
    target_column="fruit_label"
)