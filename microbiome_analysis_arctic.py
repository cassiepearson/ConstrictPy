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
        -Rewrite everything in Python 3 - Still not widely adopted may want
         to remain in 2.XX 
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
import numpy as np # NumPy statistical package, needed for networkx graphs
#import scipy as sp # SciPy package for statistical analysis
import scipy.cluster.hierarchy as hier # Heirarchical clustering functions
import networkx as nx # Network statistical package for centrality
#import matplotlib.pyplot as plt # Utility for networkx graphs

# Import custom modules and classes
from Dataset import Dataset # Dataset classes
from std_corr import StdCorr, SprCorr, KtCorr # Correlation functions
from std_stats import StdDescStats, StdDataRanking, StdCov # Descriptive stats, ranking, covariance functions
from wgcna import WGCNA # Weighted Correlation Network Analysis
from clustering import ClusteringLinkage, ClusteringSingle, ClusteringWeighted, ClusteringCentroid, ClusteringAverage # Clustering functions
from centrality import CentralityEigen, CentralityDegree, CentralityClose, CentralityBtwn # Centrality functions

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
    
    # Excel file
    excel_file = pd.ExcelFile("Prepared_Data.xlsx")

    # Import excel sheets
    sheet_2014 = Dataset("sheet_2014", excel_file.parse("sample_conditions_year_2014"))
    sheet_2016 = Dataset("sheet_2016", excel_file.parse("sample_conditions_year_2016"))
    sheet_OTU_abundance = Dataset("sheet_OTU_abundance", excel_file.parse("Sorted_OTU_Abundance"))
    sheet_2016_2014 = Dataset("sheet_2016_2014", excel_file.parse("sample_conditions_2016_2014"))
    sheet_16S_2014_OTU = Dataset("sheet_16S_2014_OTU", excel_file.parse("16S_2014_OTU"))
    sheet_16S_2016_OTU = Dataset("sheet_16S_2016_OTU", excel_file.parse("16S_2016_OTU"))
    sheet_combined_14 = Dataset("sheet_combined_14", excel_file.parse("combined_14"))
    sheet_combined_16 = Dataset("sheet_combined_16", excel_file.parse("combined_16"))

    # Create an array of imported sheets
    initial_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_OTU_abundance,
        sheet_2016_2014,
        sheet_16S_2014_OTU,
        sheet_16S_2016_OTU,
        sheet_combined_14,
        sheet_combined_16
    ]

    '''
    Descriptive statistics, Ranking, WGCNA, Covariance for each sheet
    Dataframes are added to Dataset objects
    '''
    
    # Run basic statistical analysis over all sheets in initial_dataset list
    print "\nCalculating Descriptive Statistics, Ranking, WCGNA, and Covariance..."
    for ds in initial_datasets:
        print "\tAnalysis of %s..." % (ds.name)
        ds.addStats("std_desc_stats", StdDescStats(ds.source))
        ds.addStats("std_data_ranking", StdDataRanking(ds.source))
        ds.addStats("WGCNA", WGCNA(ds.source))
        ds.addStats("std_cov", StdCov(ds.source))

    '''
    Correlation Analysis
    For each sheet of data, runs four centrality analyses. Each analysis
    is done columnwise across the dataframe.
    '''
    
    # Equivalent to initial_datasets, copy made for ease of analysis change
    corr_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_OTU_abundance,
        sheet_2016_2014,
        sheet_16S_2014_OTU,
        sheet_16S_2016_OTU
    ]

    # List of correlation functions to be run
    corr_functions = {
        "std_corr" : StdCorr,
        "spr_corr" : SprCorr,
        "kt_corr"  : KtCorr
    }

    # Run the correlation functions in corr_functions on the corr_datasets
    print "\nCalculating Correlation..."
    for ds in corr_datasets:
        print "\tAnalysis of %s..." % (ds.name)
        for cf in corr_functions:
            ds.addStats("%s" % (cf), corr_functions[cf](ds.source))
    
    '''
    Clustering Analysis
    For each sheet of data, runs four centrality analyses.
    '''
    
    # Equivalent to initial_datasets, copy made for ease of analysis change
    cluster_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_OTU_abundance,
        sheet_2016_2014,
        sheet_16S_2014_OTU,
        sheet_16S_2016_OTU
    ]

    # List of clustering functions to be run
    cluster_functions = {
        "clustering_linkage"  : ClusteringLinkage,
        "clustering_single"  : ClusteringSingle,
        "clustering_weighted" : ClusteringWeighted,
        "clustering_centroid" : ClusteringCentroid,
        "clustering_average"  : ClusteringAverage
    }

    #  Run the clustering functions in clust_functions on the cluster_datasets
    print "\nCalculating Clustering Analysis..."
    for ds in cluster_datasets:
        print "\tAnalysis of %s..." % (ds.name)
        for cf in cluster_functions:
            ds.addStats("%s" % (cf), cluster_functions[cf](ds.source))
    
    '''
    Centrality analysis
    For each sheet of data, runs four centrality analyses. Each analysis
    is between two of three columns, for a total of 12 analyses per sheet. The
    analysis is between pH, Nitrate, and Phosphate.
    '''

    # List of sheets to run the centrality functions on
    cent_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_2016_2014
    ]

    # List of centrality functions to be run
    cent_functions = {
        "eigen_centrality"       : CentralityEigen,
        "degree_centrality"      : CentralityDegree,
        "closeness_centrality"   : CentralityClose,
        "betweenness_centrality" : CentralityBtwn
    }

    # Run the listed centrality functions on the listed sheets over three
    # significant variables: pH, PO4P, and N03N
    print "\nCalculating Centrality Analysis..."
    for ds in cent_datasets:
        print "\tAnalysis of %s..." % (ds.name)
        for cf in cent_functions:
            ds.addStats(cf + "_pH_PO4", cent_functions[cf](ds.source, "pH", "PO4P_prop"))
            ds.addStats(cf + "_pH_NO3", cent_functions[cf](ds.source, "pH", "NO3N_prop"))
            ds.addStats(cf + "_PO4_NO3", cent_functions[cf](ds.source, "PO4P_prop", "NO3N_prop"))

    '''
    Combined Analysis
    This is for analysis of tables that combine both the OTU and viarable
    tables. These tables are simply the transpose of the variable and OTU 
    datasets combined and re-indexed. This allows for a cross table analysis.
    '''
   
    # List of the combined datasets
    combined_datasets = [
        sheet_combined_14,
        sheet_combined_16
    ]
    
    # Functions that can be run on the combined datasets
    combined_functions = {
        "std_desc_stats"      : StdDescStats,
        "std_ranking"         : StdDataRanking,
        "WGCNA"               : WGCNA,
        "std_cov"             : StdCov,
        "std_corr"            : StdCorr,
        "spr_corr"            : SprCorr,
        "kt_corr"             : KtCorr,
        "clustering_linkage"  : ClusteringLinkage,
        "clusterring_single"  : ClusteringSingle,
        "clustering_weighted" : ClusteringWeighted,
        "clustering_centroid" : ClusteringCentroid,
        "clustering_average"  : ClusteringAverage
    }

    # Run the combined functions on the combind datasets 
    print "\nCalculating Combined Analysis..."
    for ds in combined_datasets:
        print "\tAnalysis of %s..." % (ds.name)
        for cf in combined_functions:
            ds.addStats(cf, combined_functions[cf](ds.source))

    '''
    Output
    Print computed data for each dataset to the console
    Output all data as labelled CSV to OUTPUT_DIR
    '''

    for ds in initial_datasets:
        if (VERBOSE): ds.printStats()
        ds.statsToCSV(OUTPUT_DIR)


# Initiate the main function and prevent the others from running without being
# called
if __name__ == '__main__':
    main()
