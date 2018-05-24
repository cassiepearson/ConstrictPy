"""
Clustering
Measure of data smilarity. Hierarchical methods cluster based on distance
between nodes. K-means will not be utilized for this analysis, but will be
implemented in the generalized tool.
"""
import pandas as pd  # Necessary to handle dataframes
import numpy as np  # NumPy statistical package, needed for networkx graphs

# import scipy as sp # SciPy package for statistical analysis
import scipy.cluster.hierarchy as hier  # Heirarchical clustering functions


def ClusteringLinkage(data_frame):
    # Agglomerative clustering
    cluster_linkage = hier.linkage(data_frame)

    # Alternative cluster_return to leave the indexing in of the csv
    # cluster_return = pd.DataFrame(cluster_linkage)

    cluster_return = pd.DataFrame(
        data=cluster_linkage[1:, 1:],  # values
        index=cluster_linkage[1:, 0],  # 1st column as index
        columns=cluster_linkage[0, 1:],
    )  # 1st row as the column names

    # Check agglomerative clustering linkage validity
    cluster_linkage_validity = hier.is_valid_linkage(cluster_linkage)
    print("\tValidity of clustering linkage: %s" % (cluster_linkage_validity))

    # Return the linkage if valid
    if cluster_linkage_validity is True:
        return cluster_return
    else:
        print(
            """
        \n\n\n
         ---------------------------------------------
        | WARNING: THE CLUSTERING LINKAGE IS INVALID! |
         ---------------------------------------------
        \n\n\n
        """
        )
        return None


def ClusteringSingle(data_frame):
    # Nearest linkage on the condensed distance matrix
    cluster_single = hier.single(data_frame)

    # Alternative cluster_return to leave the indexing in of the csv
    # cluster_return = pd.DataFrame(cluster_single)

    cluster_return = pd.DataFrame(
        data=cluster_single[1:, 1:],  # values
        index=cluster_single[1:, 0],  # 1st column as index
        columns=cluster_single[0, 1:],
    )  # 1st row as the column names
    return cluster_return


def ClusteringWeighted(data_frame):
    # WPGMA linkage on the condensed distance matrix
    cluster_weighted = hier.weighted(data_frame)

    # Alternative cluster_return to leave the indexing in of the csv
    # cluster_return = pd.DataFrame(cluster_weighted)

    cluster_return = pd.DataFrame(
        data=cluster_weighted[1:, 1:],  # values
        index=cluster_weighted[1:, 0],  # 1st column as index
        columns=cluster_weighted[0, 1:],
    )  # 1st row as the column names
    return cluster_return


def ClusteringCentroid(data_frame):
    # Centroid linkage
    cluster_centroid = hier.centroid(data_frame)

    # Alternative cluster_return to leave the indexing in of the csv
    # cluster_return = pd.DataFrame(cluster_centroid)

    cluster_return = pd.DataFrame(
        data=cluster_centroid[1:, 1:],  # values
        index=cluster_centroid[1:, 0],  # 1st column as index
        columns=cluster_centroid[0, 1:],
    )  # 1st row as the column names
    return cluster_return


def ClusteringAverage(data_frame):
    # Average linkage on a condensed distance matrix
    cluster_average = hier.average(data_frame)

    # Alternative cluster_return to leave the indexing in of the csv
    # cluster_return = pd.DataFrame(cluster_average)

    cluster_return = pd.DataFrame(
        data=cluster_average[1:, 1:],  # values
        index=cluster_average[1:, 0],  # 1st column as index
        columns=cluster_average[0, 1:],
    )  # 1st row as the column names
    return cluster_return
