'''
Artic Microbiome Data Analysis
By Christopher Negrich contact at cnegrich@gmail.com
September 2017

This program is designed to allow for a variety of similar data sets to be
analyzed. Modifying the main function and splitting the rest into module(s)
as needed could generalize the functionality if needed for alternative data sets.
'''
# Import all needed packages, see documentation for details
import pandas as pd
import numpy as np # NumPy statistical package
#import scipy as sp # SciPy package for statistical analysis
#import cobra # Not yet utilized
#import matplotlib.pyplot as plt # Matplotlib for plotting data with Juypter

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
    print "Analysis of data within each sheet:\n"
    # sample_conditions_year_2014 analysis
    print "\nAnalysis of sample_conditions_year_2014 data:\n"
    StdDescStats(sheet_2014, "sheet_2014")
    StdCorrCov(sheet_2014, "sheet_2014")
    StdDataRanking(sheet_2014,1, "sheet_2014")
    WGCNA(sheet_2014, "sheet_2014")

    # sample_conditions_year_2016 analysis
    print "\nAnalysis of sample_conditions_year_2016 data:\n"
    StdDescStats(sheet_2016, "sheet_2016")
    StdCorrCov(sheet_2016, "sheet_2016")
    StdDataRanking(sheet_2016,1, "sheet_2016")
    WGCNA(sheet_2016, "sheet_2016")

    # Sorted_OTU_Abundance analysis
    print "\nAnalysis of Sorted_OTU_Abundance data:\n"
    StdDescStats(sheet_OTU_abundance, "sheet_OTU_abundance")
    StdCorrCov(sheet_OTU_abundance, "sheet_OTU_abundance")
    StdDataRanking(sheet_OTU_abundance,1, "sheet_OTU_abundance")
    WGCNA(sheet_OTU_abundance, "sheet_OTU_abundance")

    # sample_conditions_year_2016_2014 analysis
    print "\nAnalysis of sample_conditions_year_2016_2014 data:\n"
    StdDescStats(sheet_2016_2014, "sheet_2016_2014")
    StdCorrCov(sheet_2016_2014, "sheet_2016_2014")
    StdDataRanking(sheet_2016_2014,1, "sheet_2016_2014")
    WGCNA(sheet_2016_2014, "sheet_2016_2014")

    # 16S_2014_OTU analysis
    print "\nAnalysis of 16S_2014_OTU data:\n"
    StdDescStats(sheet_16S_2014_OTU, "sheet_16S_2014_OTU")
    StdCorrCov(sheet_16S_2014_OTU, "sheet_16S_2014_OTU")
    StdDataRanking(sheet_16S_2014_OTU,1, "sheet_16S_2014_OTU")
    WGCNA(sheet_16S_2014_OTU, "sheet_16S_2014_OTU")

    # 16S_2016_OTU analysis
    print "\nAnalysis of 16S_2016_OTU data:\n"
    StdDescStats(sheet_16S_2016_OTU, "sheet_16S_2016_OTU")
    StdCorrCov(sheet_16S_2016_OTU, "sheet_16S_2016_OTU")
    StdDataRanking(sheet_16S_2016_OTU,1, "sheet_16S_2016_OTU")
    WGCNA(sheet_16S_2016_OTU, "sheet_16S_2016_OTU")

    '''
    Statistics on Explanatory Factors
    '''
    print "\nStatistics on Explanatory Factors:\n"

    # 2016: pH, NO2-N
    print "Statistics of pH, NO2-N from 2016 data:"
    pH_2016_var =  sheet_2016["pH"].var()
    NO2_2016_var = sheet_2016["NO2-N"].var()
    pH_NO2_2016_cov = sheet_2016["pH"].cov(sheet_2016["NO2-N"])
    print "pH variance: " + str(pH_2016_var)
    print "NO2-N variance: " + str(NO2_2016_var)
    print "NO2-N, pH covariance: " + str(pH_NO2_2016_cov)

    # 2014 and 2016: NO2-N, NO3-N
    print "\nStatistics of NO2-N, NO3-N from 2014, 2016 data:"
    NO2_2014_16_var = sheet_2016_2014["NO2-N"].var()
    NO3_2014_16_var = sheet_2016_2014["NO3-N"].var()
    NO2_NO3_2014_16_cov = sheet_2016_2014["NO2-N"].cov(sheet_2016_2014["NO3-N"])
    print "NO2-N variance: " + str(NO2_2014_16_var)
    print "NO3-N variance: " + str(NO3_2014_16_var)
    print "NO2-N, NO3-N covariance: " + str(NO2_NO3_2014_16_cov)

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

'''
Pandas Standard Statistical Correlation
Using the data frame correlation methods built into pandas. Correlation is done
by columns, transpose for correlation by rows. This method will automatically
exclude NA/null variables.
'''
def StdCorrCov(data_frame, name):
    # Standard Correlation Coefficient - Pearson Correlation
    std_corr_frame = data_frame.corr(method="pearson")
    filename = output_dir + "std_corr_frame_" + name
    std_corr_frame.to_csv(filename)
    print "\nStandard Correlation: \n"
    print std_corr_frame

    # Spearman rank Correlation
    sprc_corr_frame = data_frame.corr(method="spearman")
    filename = output_dir + "sprc_corr_frame_" + name
    sprc_corr_frame.to_csv(filename)
    print "\nSpearman Correlation: \n"
    print sprc_corr_frame

    # Kendall Tau Correlation
    ktc_corr_frame = data_frame.corr(method="kendall")
    filename = output_dir + "ktc_corr_frame_" + name
    ktc_corr_frame.to_csv(filename)
    print "\nKendall Tau Correlation: \n"
    print ktc_corr_frame

    # Standard Covariance
    cov_frame = data_frame.cov()
    filename = output_dir + "cov_frame_" + name
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
    filename = output_dir + "wc_corr_adj_" + name
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
    filename = output_dir + "ranked_frame_" + name
    ranked_frame.to_csv(filename)
    print "\nData Frame Ranking: \n"
    print ranked_frame

'''
Partial Least Squares Data Analysis (PLSDA)
TODO
'''

'''
Subnetwork Analysis
TODO
'''

# Initiate the main function and prevent the others from running without being
# called
if __name__ == '__main__':
    main()
