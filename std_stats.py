import pandas as pd # Necessary to handle dataframes
'''
Pandas Descriptive Statistics
Basic descriptive statistics on each data frame using the built in methods for
pandas.
'''


def StdDescStats(data_frame):
    # All optional parameters excluded
    desc_stats = data_frame.describe()
    return desc_stats

'''
Pandas Standard Data Ranking
Compute numerical data ranks (1 through n) along provided axis.
'''


def StdDataRanking(data_frame):
    # Data Frame ranking, rank = 0 for rows, rank = 1 for columns
    ranked_frame = data_frame.rank(1)
    return ranked_frame

'''
Pandas Standard Covariance
Using the data frame correlation methods built into pandas. Covariance is done
by columns, transpose for covariance by rows. This method will automatically
exclude NA/null variables.
'''

def StdCov(data_frame):
    # Standard Covariance
    cov_frame = data_frame.cov()
    return cov_frame

