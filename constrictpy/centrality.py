"""
Centrality
Measure of influence of a node in a network.
"""
import pandas as pd
import numpy as np  # NumPy statistical package, needed for networkx graphs

# import scipy as sp # SciPy package for statistical analysis
import networkx as nx  # Network statistical package for centrality

# import matplotlib.pyplot as plt # Utility for networkx graphs


def CentralityEigen(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Use network x and numpy to measure node centrality
    # Measure of influence of a node
    eigen_centrality = nx.eigenvector_centrality_numpy(G)

    # return eigen_centrality as a DataFrame
    df_eigen_centrality = pd.DataFrame.from_dict(data=eigen_centrality, orient="index")
    return df_eigen_centrality


def CentralityDegree(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Number of ties a node has to another node
    degree_centrality = nx.degree_centrality(G)
    # print degree_centrality

    # return degree_centrality as a DataFrame
    df_degree_centrality = pd.DataFrame.from_dict(
        data=degree_centrality, orient="index"
    )
    return df_degree_centrality


def CentralityClose(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Sum of the shortest path lengths from a node to all other nodes
    closeness_centrality = nx.closeness_centrality(G)

    # return closeness_centrality as a DataFrame
    df_closeness_centrality = pd.DataFrame.from_dict(
        data=closeness_centrality, orient="index"
    )
    return df_closeness_centrality


def CentralityBtwn(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Measure of centrality based on shortest paths
    betweenness_centrality = nx.betweenness_centrality(G)

    # return betweenness_centrality as a DataFrame
    df_betweenness_centrality = pd.DataFrame.from_dict(
        data=betweenness_centrality, orient="index"
    )
    return df_betweenness_centrality
