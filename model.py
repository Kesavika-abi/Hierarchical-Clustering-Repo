import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler
from sklearn.cluster import AgglomerativeClustering

def perform_clustering(df, n_clusters):
    # Make a copy to avoid modifying original
    df_copy = df.copy()

    # Encode the categorical column (Meal Type)
    le = LabelEncoder()
    df_copy['MealTypeEncoded'] = le.fit_transform(df_copy['MostOrderedMealType'])

    # Select features for clustering
    features = df_copy[['TotalOrders', 'MealTypeEncoded', 'AvgOrderTime']]

    # Scale the features
    scaler = StandardScaler()
    scaled_features = scaler.fit_transform(features)

    # Apply Agglomerative Clustering
    model = AgglomerativeClustering(n_clusters=n_clusters, linkage='ward')
    labels = model.fit_predict(scaled_features)

    # Add labels to the dataframe
    df_copy['Cluster'] = labels
    return df_copy, labels
