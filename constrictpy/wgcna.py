'''
Weighted Correlation Network Analysis
Use the Pandas applymap to do a WGCNA on each sheet.
'''
import pandas as pd # Necessary to handle dataframes

def WGCNA(data_frame):
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