import pytest
import pandas as pd
from constrictpy import rfunctions

"""
In its current state, this module tests imported R functions using a new
pandas DataFrame with some numbers. As R functions are implemented, these
tests will be conducted using the 'Prepared_Data.xlsx' data file.
"""

# get Dict of R packages
constrictr_packages = rfunctions.source_packages()


def test_desc_stats():
    # define desc_stats function
    desc_stats = constrictr_packages["desc_stats"].desc_stats
    # set up test environment
    data = [1, 1, 2, 3, 5, 8, 13]
    df = pd.DataFrame(data)
    result = rfunctions.r_to_pandas(desc_stats(df))

    assert result["mean"][1] == 4.714285714285714
    assert result["var"][1] == 19.571428571428573
    assert result["sd"][1] == 4.423960733486292
    assert result["se"][1] == 1.6720999872456608


# TODO: test adj_matrix

# TODO: test banner

# TODO: test centrality

# TODO: test clust

# TODO: test corr

# TODO: test covar

# TODO: test df_rank

# TODO: test rank

# TODO: test sparse

# TODO: test sparsity

# TODO: test wcgna
