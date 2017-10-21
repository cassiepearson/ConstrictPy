'''
Pandas Standard Statistical Correlation Methods
Using the data frame correlation methods built into pandas. Correlation is done
by columns, transpose for correlation by rows. This method will automatically
exclude NA/null variables.
'''
import pandas as pd # Necessary to handle dataframes

def StdCorr(data_frame):
    # Standard Correlation Coefficient - Pearson Correlation
    std_corr_frame = data_frame.corr(method="pearson")
    return std_corr_frame


def SprCorr(data_frame):
    # Spearman rank Correlation
    sprc_corr_frame = data_frame.corr(method="spearman")
    return sprc_corr_frame


def KtCorr(data_frame):
    # Kendall Tau Correlation
    ktc_corr_frame = data_frame.corr(method="kendall")
    return ktc_corr_frame