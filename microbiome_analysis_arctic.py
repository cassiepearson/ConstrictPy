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
import scipy.cluster.hierarchy as hier # Wild card imported for methods testing
import networkx as nx

'''
Data output - Defines output behavior
'''
# Define output directory
output_dir = "output-files/"


'''
Main function
'''
def main():
    '''
    Data import - Originally was separated function, hard coded for convience
    '''
    # Load spreadsheet
    excel_file = pd.ExcelFile("Prepared_Data.xlsx")
    # Load each sheet into a separate dataframe
    sheet_2014 = excel_file.parse("sample_conditions_year_2014")
    sheet_2016 = excel_file.parse("sample_conditions_year_2016")
    sheet_OTU_abundance = excel_file.parse("Sorted_OTU_Abundance")
    sheet_2016_2014 = excel_file.parse("sample_conditions_year_2016_2014")
    sheet_16S_2014_OTU = excel_file.parse("16S_2014_OTU")
    sheet_16S_2016_OTU = excel_file.parse("16S_2016_OTU")


    '''
    Analysis of all data within each sheet
    '''
    initial_frames = {"sheet_2014"          : sheet_2014,
                      "sheet_2016"          : sheet_2016,
                      "sheet_OTU_abundance" : sheet_OTU_abundance,
                      "sheet_2016_2014"     : sheet_2016_2014,
                      "sheet_16S_2014_OTU"  : sheet_16S_2014_OTU,
                      "sheet_16S_2016_OTU"  : sheet_16S_2016_OTU,
                     }

    # ***Needs to be altered to handle returns and new function names
    print "Analysis of data within each sheet:\n"
    for label in initial_frames:
        print "\nAnalysis of " + label + "\n"
        StdDescStats(initial_frames[label], label)
        StdCorr(initial_frames[label], label)
        StdDataRanking(initial_frames[label], 1, label)
        WGCNA(initial_frames[label], label)


    '''
    Statistics on Explanatory Factors
    '''
    #print "\nStatistics on Explanatory Factors:\n"

    # 2016: pH, NO2-N
    #print "Statistics of pH, NO2-N from 2016 data:"
    #pH_2016_var =  sheet_2016["pH"].var()
    #NO2_2016_var = sheet_2016["NO2-N"].var()
    #pH_NO2_2016_cov = sheet_2016["pH"].cov(sheet_2016["NO2-N"])
    #print "pH variance: " + str(pH_2016_var)
    #print "NO2-N variance: " + str(NO2_2016_var)
    #print "NO2-N, pH covariance: " + str(pH_NO2_2016_cov)

'''
Pandas Descriptive Statistics
Basic descriptive statistics on each data frame using the built in methods for
pandas.
'''
def StdDescStats(data_frame, name):
    # All optional parameters excluded
    desc_stats = data_frame.describe()
    filename = output_dir + "desc_stats_" + name
    desc_stats.to_csv(filename)
    print "\nDescriptive Statistics: \n"
    print desc_stats
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
    filename = output_dir + "std_corr_frame_" + name
    std_corr_frame.to_csv(filename)
    print "\nStandard Correlation: \n"
    print std_corr_frame
    return std_corr_frame

def SprCorr(data_frame, name):
    # Spearman rank Correlation
    sprc_corr_frame = data_frame.corr(method="spearman")
    filename = output_dir + "sprc_corr_frame_" + name
    sprc_corr_frame.to_csv(filename)
    print "\nSpearman Correlation: \n"
    print sprc_corr_frame
    return sprc_corr_frame

def KtCorr(data_frame, name):
    # Kendall Tau Correlation
    ktc_corr_frame = data_frame.corr(method="kendall")
    filename = output_dir + "ktc_corr_frame_" + name
    ktc_corr_frame.to_csv(filename)
    print "\nKendall Tau Correlation: \n"
    print ktc_corr_frame
    return ktc_corr_frame

def StdCov(data_frame, name):
    # Standard Covariance
    cov_frame = data_frame.cov()
    filename = output_dir + "cov_frame_" + name
    cov_frame.to_csv(filename)
    print "\nPairwise Covariance: \n"
    print cov_frame
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
    #wc_adj_log = np.log(wc_corr_adj)
    #print wc_adj_log

    # Export to csv
    filename = output_dir + "wc_corr_adj_" + name
    wc_corr_adj.to_csv(filename)

    print '\nWeighted Correlation Network Analysis Matrix:\n'
    print wc_corr_adj
    return wc_corr_adj

'''
Pandas Standard Data Ranking
Compute numerical data ranks (1 through n) along provided axis.
'''
def StdDataRanking(data_frame, rank, name):
    # Data Frame ranking, rank = 0 for rows, rank = 1 for columns
    ranked_frame = data_frame.rank(rank)
    filename = output_dir + "ranked_frame_" + name
    ranked_frame.to_csv(filename)
    print "\nData Frame Ranking: \n"
    print ranked_frame
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
    if(cluster_linkage_validity == True): return cluster_linkage

def ClusteringSingle(data_frame):
    # Nearest linkage on the condensed distance matrix
    cluster_single = hier.single(data_frame)
    print cluster_single
    return cluster_single

def ClusteringWeighted(data_frame):
    # WPGMA linkage on the condensed distance matrix
    cluster_weighted = hier.weighted(data_frame)
    print cluster_weighted
    return cluster_weighted

def ClusteringCentroid(data_frame):
    # Centroid linkage
    cluster_centroid = hier.centroid(data_frame)
    print cluster_centroid
    return cluster_centroid

def ClusteringAverage(data_frame):
    # Average linkage on a condensed distance matrix
    cluster_average = hier.average(data_frame)
    print cluster_average
    return cluster_average

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
    print eigen_centrality
    return eigen_centrality

def CentralityDegree(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Number of ties a node has to another node
    degree_centrality = nx.degree_centrality(G)
    print degree_centrality
    return degree_centrality

def CentralityClose(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Sum of the shortest path lengths from a node to all other nodes
    closeness_centrality = nx.closeness_centrality(G)
    print closeness_centrality
    return closeness_centrality

def CentralityBtwn(data_frame, source, target):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Measure of centrality based on shortest paths
    betweenness_centrality = nx.betweenness_centrality(G)
    print betweenness_centrality
    return betweenness_centrality

# Initiate the main function and prevent the others from running without being
# called
if __name__ == '__main__':
    main()
