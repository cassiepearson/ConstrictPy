'''
Artic Microbiome Data Analysis
Authored by:
    Christopher Negrich contact at cnegrich@gmail.com
    Andrew Hoetker contact at ahoetker@asu.edu
    Courtney Johnson contact at cejohn32@asu.edu
Last Updated: October 2017

This program is designed to allow for a variety of similar data sets to be
analyzed. Modifying the main function and splitting the rest into module(s)
as needed could generalize the functionality if needed for alternative data sets.

Modifications for generalization into tool (next step):
    //TODO:
        -Rewrite everything in Python 3
        -Prepare a formalized and breif project style guide

        -Port all documentation to github
        -Background research - Citations
        -Create a user interface (Chris)
        -Create a robust file import/export functions
            -Ask Dr. Cao about what programs we will be taking input from
        -Write mathematical documentation for implementations
        -Port algorithms to R
        -Create functions for graphing
        -Further subdivide and enumerate possible algorithms
            -Allow for as much user choice as possible
        -Find test data sets - Random data, other experimental data

For internal team reference:
    -Search "***" for high priority changes
'''
# Import all needed packages, see documentation for details
import pandas as pd
import numpy as np # NumPy statistical package
#import scipy as sp # SciPy package for statistical analysis
import scipy.cluster.hierarchy as hier # Methods testing
import networkx as nx # Network statistical package for centrality
import matplotlib.pyplot as plt # Utility for networkx graphs
from Dataset import Dataset # Dataset.py


'''
Main function
'''


def main():
    '''
    Define Constants
    Set the output directory
    Choose whether to print stats summary to console
    '''
    OUTPUT_DIR = "output-files/"
    VERBOSE = False

    '''
    Data Import
    Parse sheets of the excel data into six Dataset objects as dataset.source
    '''
    excel_file = pd.ExcelFile("Prepared_Data.xlsx")

    sheet_2014 = Dataset("sheet_2014", excel_file.parse("sample_conditions_year_2014"))
    sheet_2016 = Dataset("sheet_2016", excel_file.parse("sample_conditions_year_2016"))
    sheet_OTU_abundance = Dataset("sheet_OTU_abundance", excel_file.parse("Sorted_OTU_Abundance"))
    sheet_2016_2014 = Dataset("sheet_2016_2014", excel_file.parse("sample_conditions_2016_2014"))
    sheet_16S_2014_OTU = Dataset("sheet_16S_2014_OTU", excel_file.parse("16S_2014_OTU"))
    sheet_16S_2016_OTU = Dataset("sheet_16S_2016_OTU", excel_file.parse("16S_2016_OTU"))

    initial_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_OTU_abundance,
        sheet_2016_2014,
        sheet_16S_2014_OTU,
        sheet_16S_2016_OTU
    ]

    '''
    Descriptive statistics for each sheet
    Dataframes are added to Dataset objects
    '''
    print "Calculating Descriptive Statistics"
    for ds in initial_datasets:
        print "\n Analysis of " + ds.name + "\n"
        ds.addStats("StdDescStats", StdDescStats(ds.source, ds.name))
        ds.addStats("StdCorr", StdCorr(ds.source, ds.name))
        ds.addStats("StdDataRanking", StdDataRanking(ds.source, 1, ds.name))
        ds.addStats("WGCNA", WGCNA(ds.source, ds.name))

    '''
    Centrality analysis
    For each sheet of data, runs four centrality analyses. Each analysis
    is between two of three columns, for a total of 12 analyses per sheet. The
    analysis is between pH, Nitrate, and Phosphate.
    '''

    sample_cond_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_2016_2014
    ]

    cent_functions = {
        "eigen_centrality": CentralityEigen,
        "degree_centrality": CentralityDegree,
        "closeness_centrality": CentralityClose,
        "betweenness_centrality": CentralityBtwn
    }


    print "Calculating Centrality Statistics"
    for ds in sample_cond_datasets:
        print "\n Analysis of " + ds.name + "\n"
        for cf in cent_functions:
            ds.addStats(cf + "_pH_PO4", cent_functions[cf](ds.source, "pH", "PO4P_prop"))
            ds.addStats(cf + "_pH_NO3", cent_functions[cf](ds.source, "pH", "NO3N_prop"))
            ds.addStats(cf + "_PO4_NO3", cent_functions[cf](ds.source, "PO4P_prop", "NO3N_prop"))

    '''
    Output
    Print computed data for each dataset to the console
    Output all data as labelled CSV to OUTPUT_DIR
    '''

    for ds in initial_datasets:
        if (VERBOSE): ds.printStats()
        ds.statsToCSV(OUTPUT_DIR)


'''
Pandas Descriptive Statistics
Basic descriptive statistics on each data frame using the built in methods for
pandas.
'''


def StdDescStats(data_frame, name):
    # All optional parameters excluded
    desc_stats = data_frame.describe()
    return desc_stats


'''
Pandas Standard Statistical Correlation Methods
Using the data frame correlation methods built into pandas. Correlation is done
by columns, transpose for correlation by rows. This method will automatically
exclude NA/null variables.
'''


def StdCorr(data_frame, name):
    # Standard Correlation Coefficient - Pearson Correlation
    std_corr_frame = data_frame.corr(method="pearson")
    return std_corr_frame


def SprCorr(data_frame, name):
    # Spearman rank Correlation
    sprc_corr_frame = data_frame.corr(method="spearman")
    return sprc_corr_frame


def KtCorr(data_frame, name):
    # Kendall Tau Correlation
    ktc_corr_frame = data_frame.corr(method="kendall")
    return ktc_corr_frame


def StdCov(data_frame, name):
    # Standard Covariance
    cov_frame = data_frame.cov()
    return cov_frame


'''
Weighted Correlation Network Analysis
Use the Pandas applymap to do a WGCNA on each sheet.
'''


def WGCNA(data_frame, name):
    # Create the Pearson Correlation Matrix
    wc_corr = data_frame.corr(method="pearson")

    # Create the unsigned Matrix
    wc_corr_us = wc_corr.abs()

    # Create the signed matrix
    wc_corr_s = wc_corr_us.applymap(lambda x: 0.5+0.5*x)

    # Apply thresholding parameter (6 or 12 standard) to create adjacentcy matrix
    wc_corr_adj = wc_corr_s.applymap(lambda x: x**6)

    # Take the log if desired (to show the linear relation to the co-expression similarity)
    # wc_adj_log = np.log(wc_corr_adj)
    # print wc_adj_log

    return wc_corr_adj


'''
Pandas Standard Data Ranking
Compute numerical data ranks (1 through n) along provided axis.
'''


def StdDataRanking(data_frame, rank, name):
    # Data Frame ranking, rank = 0 for rows, rank = 1 for columns
    ranked_frame = data_frame.rank(rank)
    return ranked_frame


'''
Clustering
Measure of data smilarity. Hierarchical methods cluster based on distance
between nodes. K-means will not be utilized for this analysis, but will be
implemented in the generalized tool.
'''


def ClusteringLinkage(data_frame):
    # Agglomerative clustering
    cluster_linkage = hier.linkage(data_frame)
    print cluster_linkage

    # Check agglomerative clustering linkage validity
    cluster_linkage_validity = hier.is_valid_linkage(cluster_linkage)
    print "\nValidity of clustering linkage: " + cluster_linkage_validity + "\n"

    # Return the linkage if valid
    if cluster_linkage_validity is True:
        return cluster_linkage
    else:
        return None


def ClusteringSingle(data_frame):
    # Nearest linkage on the condensed distance matrix
    cluster_single = hier.single(data_frame)
    print cluster_single


def ClusteringWeighted(data_frame):
    # WPGMA linkage on the condensed distance matrix
    cluster_weighted = hier.weighted(data_frame)
    print cluster_weighted


def ClusteringCentroid(data_frame):
    # Centroid linkage
    cluster_centroid = hier.centroid(data_frame)
    print cluster_centroid


def ClusteringAverage(data_frame):
    # Average linkage on a condensed distance matrix
    cluster_average = hier.average(data_frame)
    print cluster_average


'''
Centrality
Measure of influence of a node in a network.
'''


def CentralityEigen(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Use network x and numpy to measure node centrality
    # Measure of influence of a node
    eigen_centrality = nx.eigenvector_centrality_numpy(G)

    # return eigen_centrality as a DataFrame
    df_eigen_centrality = pd.DataFrame.from_dict(data=eigen_centrality, orient='index')
    return df_eigen_centrality


def CentralityDegree(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Number of ties a node has to another node
    degree_centrality = nx.degree_centrality(G)
    # print degree_centrality

    # return degree_centrality as a DataFrame
    df_degree_centrality = pd.DataFrame.from_dict(data=degree_centrality, orient='index')
    return df_degree_centrality


def CentralityClose(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Sum of the shortest path lengths from a node to all other nodes
    closeness_centrality = nx.closeness_centrality(G)

    # return closeness_centrality as a DataFrame
    df_closeness_centrality = pd.DataFrame.from_dict(data=closeness_centrality, orient='index')
    return df_closeness_centrality


def CentralityBtwn(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Measure of centrality based on shortest paths
    betweenness_centrality = nx.betweenness_centrality(G)

    # return betweenness_centrality as a DataFrame
    df_betweenness_centrality = pd.DataFrame.from_dict(data=betweenness_centrality, orient='index')
    return df_betweenness_centrality


# Initiate the main function and prevent the others from running without being
# called
if __name__ == '__main__':
    main()
