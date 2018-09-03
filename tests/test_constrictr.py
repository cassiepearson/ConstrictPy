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



# TODO: test adj_matrix
def test_adj_matrix():
    for key in constrictr_packages:
        print("{}: {}".format(key, constrictr_packages[key]))

    adj_matrix = constrictr_packages["adj_matrix"].adj_matrix
    assert type(adj_matrix) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_ap_short():
    aPairsShortest = constrictr_packages["ap_short"].aPairsShortest
    assert type(aPairsShortest) == rpy2.robjects.functions.SignatureTranslatedFunction


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
    cent = constrictr_packages["centrality"].cent
    assert type(cent) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_closeness_centrality():
    closCent = constrictr_packages["closeness_centrality"].closCent
    assert type(closCent) == rpy2.robjects.functions.SignatureTranslatedFunction


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

def test_CR_kBounds():
    boundSetup = constrictr_packages["CR-kBounds"].boundSetup
    assert type(boundSetup) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_CR_kCHelp():
    CR_kCHelp = constrictr_packages["CR-kCHelp"]
    assert type(CR_kCHelp.moveCents) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kCHelp.updateBounds) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kCHelp.dist2All) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_CR_kCluster():
    CR_kCluster = constrictr_packages["CR-kCluster"]
    assert type(CR_kCluster.boundSetup) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kCluster.kClustering) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_CR_kCSetup():
    CR_kCSetup = constrictr_packages["CR-kCSetup"]
    assert type(CR_kCSetup.resetVars) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kCSetup.setup) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_CR_kMean():
    CR_kMean = constrictr_packages["CR-kMean"]
    assert type(CR_kMean.kSingle) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kMean.cleanup) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kMean.cRKMPP) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_CR_kSeeding():
    CR_kSeeding = constrictr_packages["CR-kSeeding"]
    assert type(CR_kSeeding.sPP) == rpy2.robjects.functions.SignatureTranslatedFunction
    assert type(CR_kSeeding.kMPPSeed) == rpy2.robjects.functions.SignatureTranslatedFunction


def test_degree_centrality():
    degree_centrality = constrictr_packages["degree_centrality"]
    assert type(degree_centrality.degCent) == rpy2.robjects.functions.SignatureTranslatedFunction


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

def test_df_rank():
    # TODO: Write functionality tests for df_rank
    df_rank = constrictr_packages["df_rank"].df_rank
    assert type(df_rank) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_dist_matrix():
    dist_matrix = constrictr_packages["dist_matrix"]
    assert type(dist_matrix.distMatrix) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_dist_metric():
    dist_metric = constrictr_packages["dist_metric"]
    assert type(dist_metric.adjMatrix) == rpy2.robjects.functions.SignatureTranslatedFunction

def test_hierarchical():
    hierarchical = constrictr_packages["hierarchical"]
    assert type(hierarchical.hierarchical) == rpy2.robjects.functions.SignatureTranslatedFunction

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

def test_topo_matrix():
    topo_matrix = constrictr_packages["topo_matrix"]
    assert type(topo_matrix.topOMatrix) == rpy2.robjects.functions.SignatureTranslatedFunction

