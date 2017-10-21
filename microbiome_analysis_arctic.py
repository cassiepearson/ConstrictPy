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
import matplotlib.pyplot as plt # The Dark Lord hears our prayer and is pleased

'''
Data output - Defines output behavior
'''
# Define output directory
OUTPUT_DIR = "output-files/"


'''
Main function
'''
def main():
    '''
    Data import
    Once again, this is just calling a function with hardcoded values
    '''
    initial_frames = importSheetsToFrames("Prepared_Data.xlsx")

    '''
    Descriptive statistics for each sheet
    All dataframes are exported to CSV
    '''
    print "Analysis of data within each sheet:\n"
    for label in initial_frames:
        print "\nAnalysis of " + label + "\n"
        StdDescStats(initial_frames[label], label)
        StdCorr(initial_frames[label], label)
        StdDataRanking(initial_frames[label], 1, label)
        WGCNA(initial_frames[label], label)

    '''
    Centrality analysis
    For each sheet of data, runs four centrality analyses. Each analysis
    is between two of three columns, for a total of 12 analyses per sheet. The
    analysis is between pH, Nitrate, and Phosphate. 
    '''
    
    sample_cond_frames = [
                        "sheet_2014",
                        "sheet_2016",
                        "sheet_2016_2014"
                          ]
    
    centrality_functions = [
                            CentralityEigen, 
                            CentralityDegree, 
                            CentralityClose,
                            CentralityBtwn
                            ]
    
    for label in sample_cond_frames:
        for cf in centrality_functions:
            cf(initial_frames[label], "pH", "PO4P_prop", label + "_pH_PO4")
            cf(initial_frames[label], "pH", "NO3N_prop", label + "_pH_NO3")
            cf(initial_frames[label], "PO4P_prop", "NO3N_prop", label + "_PO4_NO3")


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
Import Function
Basically just a macro
'''
def importSheetsToFrames(excel_filename):
    # Load spreadsheet
    excel_file = pd.ExcelFile(str(excel_filename))
    # Load each sheet into a separate dataframe
    sheet_2014 = excel_file.parse("sample_conditions_year_2014")
    sheet_2014 = excel_file.parse("sample_conditions_year_2014")
    sheet_2016 = excel_file.parse("sample_conditions_year_2016")
    sheet_OTU_abundance = excel_file.parse("Sorted_OTU_Abundance")
    sheet_2016_2014 = excel_file.parse("sample_conditions_2016_2014")
    sheet_16S_2014_OTU = excel_file.parse("16S_2014_OTU")
    sheet_16S_2016_OTU = excel_file.parse("16S_2016_OTU")
    # Make dictionary of initially imported DataFrames
    import_frames = {"sheet_2014"          : sheet_2014,
                     "sheet_2016"          : sheet_2016,
                     "sheet_OTU_abundance" : sheet_OTU_abundance,
                     "sheet_2016_2014"     : sheet_2016_2014,
                     "sheet_16S_2014_OTU"  : sheet_16S_2014_OTU,
                     "sheet_16S_2016_OTU"  : sheet_16S_2016_OTU,
                     }
    return import_frames
    

'''
Pandas Descriptive Statistics
Basic descriptive statistics on each data frame using the built in methods for
pandas.
'''
def StdDescStats(data_frame, name):
    # All optional parameters excluded
    desc_stats = data_frame.describe()
    filename = OUTPUT_DIR + "desc_stats_" + name
    desc_stats.to_csv(filename)
    print "\nDescriptive Statistics: \n"
    print desc_stats

'''
Pandas Standard Statistical Correlation Methods
Using the data frame correlation methods built into pandas. Correlation is done
by columns, transpose for correlation by rows. This method will automatically
exclude NA/null variables.
'''
def StdCorr(data_frame, name):
    # Standard Correlation Coefficient - Pearson Correlation
    std_corr_frame = data_frame.corr(method="pearson")
    filename = OUTPUT_DIR + "std_corr_frame_" + name
    std_corr_frame.to_csv(filename)
    print "\nStandard Correlation: \n"
    print std_corr_frame

def SprCorr(data_frame, name):
    # Spearman rank Correlation
    sprc_corr_frame = data_frame.corr(method="spearman")
    filename = OUTPUT_DIR + "sprc_corr_frame_" + name
    sprc_corr_frame.to_csv(filename)
    print "\nSpearman Correlation: \n"
    print sprc_corr_frame

def KtCorr(data_frame, name):
    # Kendall Tau Correlation
    ktc_corr_frame = data_frame.corr(method="kendall")
    filename = OUTPUT_DIR + "ktc_corr_frame_" + name
    ktc_corr_frame.to_csv(filename)
    print "\nKendall Tau Correlation: \n"
    print ktc_corr_frame

def StdCov(data_frame, name):
    # Standard Covariance
    cov_frame = data_frame.cov()
    filename = OUTPUT_DIR + "cov_frame_" + name
    cov_frame.to_csv(filename)
    print "\nPairwise Covariance: \n"
    print cov_frame

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
    filename = OUTPUT_DIR + "wc_corr_adj_" + name
    wc_corr_adj.to_csv(filename)

    print '\nWeighted Correlation Network Analysis Matrix:\n'
    print wc_corr_adj


'''
Pandas Standard Data Ranking
Compute numerical data ranks (1 through n) along provided axis.
'''
def StdDataRanking(data_frame, rank, name):
    # Data Frame ranking, rank = 0 for rows, rank = 1 for columns
    ranked_frame = data_frame.rank(rank)
    filename = OUTPUT_DIR + "ranked_frame_" + name
    ranked_frame.to_csv(filename)
    print "\nData Frame Ranking: \n"
    print ranked_frame


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
    if cluster_linkage_validity == True:
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
def CentralityEigen(data_frame, source, target, name):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Use network x and numpy to measure node centrality
    # Measure of influence of a node
    eigen_centrality = nx.eigenvector_centrality_numpy(G)

    #print eigen_centrality
    
    # save a data frame of eigencentrality
    df_eigen_centrality = pd.DataFrame.from_dict(data=eigen_centrality, orient='index')
    df_eigen_centrality.to_csv(OUTPUT_DIR + "eigen_centrality_" + name)

def CentralityDegree(data_frame, source, target, name):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)
    
    

    # Number of ties a node has to another node
    degree_centrality = nx.degree_centrality(G)
    #print degree_centrality
    
    # save a data frame of degree centrality
    df_degree_centrality = pd.DataFrame.from_dict(data=degree_centrality, orient='index')
    df_degree_centrality.to_csv(OUTPUT_DIR + "degree_centrality_" + name)

def CentralityClose(data_frame, source, target, name):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)

    # Sum of the shortest path lengths from a node to all other nodes
    closeness_centrality = nx.closeness_centrality(G)
    #print closeness_centrality

#    # Create graph and save as image
#    nx.draw(G)
#    nx.draw_random(G)
#    nx.draw_circular(G)
#    nx.draw_spectral(G)
#    png_fname = OUTPUT_DIR + "networkx_graph_" + name + ".png"
#    plt.savefig(png_fname)
    
    # save a data frame of closeness centrality
    df_closeness_centrality = pd.DataFrame.from_dict(data=closeness_centrality, orient='index')
    df_closeness_centrality.to_csv(OUTPUT_DIR + "closeness_centrality_" + name)

def CentralityBtwn(data_frame, source, target, name):
    # Create a NetworkX graph
    G = nx.from_pandas_dataframe(data_frame, source, target, True)
    

    # Measure of centrality based on shortest paths
    betweenness_centrality = nx.betweenness_centrality(G)

    #print betweenness_centrality
    
     # save a data frame of betweenness centrality
    df_betweenness_centrality = pd.DataFrame.from_dict(data=betweenness_centrality, orient='index')
    df_betweenness_centrality.to_csv(OUTPUT_DIR + "betweenness_centrality_" + name)
    
# Initiate the main function and prevent the others from running without being
# called
if __name__ == '__main__':
    main()
