import matplotlib.pyplot as plt
import seaborn as sns
import os

def create_cluster_plot(df, labels):
    plt.figure(figsize=(8, 6))
    sns.scatterplot(
        x='TotalOrders',
        y='AvgOrderTime',
        hue=labels,
        palette='viridis',
        data=df,
        s=100,
        edgecolor='black'
    )
    plt.title("Food Order Clustering")
    plt.xlabel("Total Orders")
    plt.ylabel("Average Order Time")
    plt.legend(title="Cluster")
    
    plot_path = os.path.join("static", "cluster_plot.png")
    plt.savefig(plot_path)
    plt.close()
    return plot_path
