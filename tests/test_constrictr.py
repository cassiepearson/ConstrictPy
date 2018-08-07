import pytest
import pandas as pd
import rpy2.robjects.vectors
import rpy2.robjects.functions
from constrictpy import rfunctions

"""
In its current state, this module tests imported R functions using a new
pandas DataFrame with some numbers. As R functions are implemented, these
tests will be conducted using the 'Prepared_Data.xlsx' data file.

Each function tests one ConstrictR package. Each test begins by defining the function
to be tested, and checking that it is a SignatureTranslatedFunction.
"""

# get Dict of R packages
constrictr_packages = rfunctions.source_packages()


def test_desc_stats():
    desc_stats = constrictr_packages["desc_stats"].desc_stats
    assert type(desc_stats) == rpy2.robjects.functions.SignatureTranslatedFunction

    # set up test environment
    data = [1, 1, 2, 3, 5, 8, 13]
    df = pd.DataFrame(data)
    result = rfunctions.r_to_pandas(desc_stats(df))
    assert result["mean"][1] == 4.714285714285714
    assert result["var"][1] == 19.571428571428573
    assert result["sd"][1] == 4.423960733486292
    assert result["se"][1] == 1.6720999872456608


# TODO: test adj_matrix
def test_adj_matrix():
    adj_matrix = constrictr_packages["adj_matrix"].adj_matrix
    assert type(adj_matrix) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_banner():
    banner = constrictr_packages["banner"].banner
    assert type(banner) == rpy2.robjects.functions.SignatureTranslatedFunction
    result = banner()
    assert type(result) == rpy2.robjects.vectors.StrVector


def test_centrality():
    """
    This test fails because centrality.R is unfinished and cannot be sourced.
    #TODO: Write functionality tests for centrality
    """
    centrality = constrictr_packages["centrality"].centrality
    assert type(centrality) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_clust():
    """
    This test fails because clust.R is unfinished and cannot be sourced.
    TODO: Write functionality tests for clust
    """
    clust = constrictr_packages["clust"].clust
    assert type(clust) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_corr():
    # TODO: Write functionality tests for corr
    corr = constrictr_packages["corr"].corr
    assert type(corr) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_covar():
    # TODO: Write functionality tests for covar
    covar = constrictr_packages["covar"].covar
    assert type(covar) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_df_rank():
    # TODO: Write functionality tests for df_rank
    df_rank = constrictr_packages["df_rank"].df_rank
    assert type(df_rank) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_rank():
    # TODO: Write functionality tests for rank
    rank = constrictr_packages["rank"].rank
    assert type(rank) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_sparse():
    # TODO: Write functionality tests for sparse
    sparse = constrictr_packages["sparse"].sparse
    assert type(sparse) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_sparsity():
    # TODO: Write functionality tests for sparsity
    sparsity = constrictr_packages["sparsity"].sparsity
    assert type(sparsity) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_wcgna():
    """
    It's WGCNA: WeiGhted Correlation Network Analysis
    Fixing the wcgna.R filename will make this test pass.
    TODO: Fix wcgna.R filename and its string in constrictpy.rfunctions
    TODO: Write functionality tests for wgcna
    """
    wcgna = constrictr_packages["wcgna"].wcgna
    assert type(wcgna) == rpy2.robjects.functions.SignatureTranslatedFunction
