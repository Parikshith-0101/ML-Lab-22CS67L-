import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

from sklearn.cluster import KMeans
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.decomposition import PCA
from sklearn.metrics import silhouette_score


# Function for K-Means Clustering

def perform_kmeans(dataset_name, file_path, n_clusters=3):

    print("\n" + "="*70)
    print(f"DATASET: {dataset_name}")
    print("="*70)

    # Load Dataset
    df = pd.read_csv(file_path)

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nDataset Shape:", df.shape)

    
    # Handle Missing Values
    
    df = df.dropna()

    
    # Convert Categorical Columns to Numeric
    
    encoder = LabelEncoder()

    for column in df.columns:
        if df[column].dtype == 'object':
            df[column] = encoder.fit_transform(df[column])

    
    # Feature Scaling
    
    scaler = StandardScaler()
    X_scaled = scaler.fit_transform(df)

    
    # K-Means Clustering
    
    kmeans = KMeans(
        n_clusters=n_clusters,
        random_state=42,
        n_init=10
    )

    labels = kmeans.fit_predict(X_scaled)

    # Cluster Centers
    centroids = kmeans.cluster_centers_

    print("\nCluster Labels:")
    print(labels)

    print("\nCluster Centroids:")
    print(centroids)

    
    # Evaluation
    
    silhouette = silhouette_score(X_scaled, labels)

    print("\nSilhouette Score:", round(silhouette, 4))

    
    # Dimensionality Reduction for Visualization
    
    pca = PCA(n_components=2)

    X_pca = pca.fit_transform(X_scaled)

    centroid_pca = pca.transform(centroids)

    
    # Visualization
    
    plt.figure(figsize=(10, 6))

    plt.scatter(
        X_pca[:, 0],
        X_pca[:, 1],
        c=labels,
        cmap='viridis',
        s=50
    )

    # Plot Centroids
    plt.scatter(
        centroid_pca[:, 0],
        centroid_pca[:, 1],
        marker='X',
        color='red',
        s=300,
        label='Centroids'
    )

    plt.title(f"K-Means Clustering - {dataset_name}")
    plt.xlabel("PCA Component 1")
    plt.ylabel("PCA Component 2")

    plt.legend()
    plt.grid(True)

    plt.show()



# Run K-Means on All Datasets


perform_kmeans(
    dataset_name="Fruits Dataset",
    file_path="fruits.csv",
    n_clusters=3
)

perform_kmeans(
    dataset_name="Glass Dataset",
    file_path="glass.csv",
    n_clusters=3
)

perform_kmeans(
    dataset_name="Titanic Dataset",
    file_path="Titanic-Dataset.csv",
    n_clusters=3
)

perform_kmeans(
    dataset_name="Toyota Corolla Dataset",
    file_path="ToyotaCorolla.csv",
    n_clusters=3
)

perform_kmeans(
    dataset_name="Weather Forecast Dataset",
    file_path="weather_forecast.csv",
    n_clusters=3
)