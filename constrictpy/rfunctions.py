"""
Initialize the R portion of the program by activating pandas2ri
and sourcing the functions from ConstrictR.

This module has more code at the module-level than any other. It is meant to create
a static Dict of packages from ConstrictR, accessible from the main program.
"""

from rpy2.robjects import pandas2ri
from rpy2.robjects.packages import SignatureTranslatedAnonymousPackage
import rpy2.robjects.vectors
import os
import pkg_resources
import pandas as pd
from constrictpy.logger import getLogger
from typing import Dict


# define module-level logger
logger = getLogger(__name__, "info")

# activate rpy2
pandas2ri.activate()


def r_to_pandas(r_df: rpy2.robjects.vectors.DataFrame) -> pd.DataFrame:
    """
    This is essentially a macro to convert R DataFrames to pandas DataFrames
    """
    pandas_df = pandas2ri.ri2py_dataframe(r_df)
    return pandas_df


def file_to_anonymous_package(file: str) -> SignatureTranslatedAnonymousPackage:
    """
    Takes some file.R and sources it in rpy2 as an anonymous package
    Returns the R package as an object
    The name of the package is accessible by package.__rname__ as str
    """
    package_name = os.path.splitext(os.path.split(file)[1])[0]
    with open(file, "r") as r_package_file:
        r_package_src = r_package_file.read()
    package_src = SignatureTranslatedAnonymousPackage(r_package_src, name=package_name)
    return package_src


def source_packages() -> Dict[str, SignatureTranslatedAnonymousPackage]:
    """
    Define the list of package files to source, and then do it.
    Return the packages in a Dict
    This is the purpose of the whole file
    """
    # Define R packages directory, and the package files to be imported
    r_dir = pkg_resources.resource_filename("ConstrictR", "")
    r_package_files = [
        "adj_matrix.R",
        "banner.R",
        "centrality.R",
        "clust.R",
        "corr.R",
        "covar.R",
        "desc_stats.R",
        "df_rank.R",
        "rank.R",
        "sparse.R",
        "sparsity.R",
        "wcgna.R",
    ]

    # Initialize module-level Dict of R packages, indexed by string
    sourced_r_packages = {}
    """
    The previous line was,
    #sourced_r_packages: Dict[str, SignatureTranslatedAnonymousPackage] = {}
    but variable type annotations are not supported in python <3.6.x
    """
    # add packages to the module-level Dict
    for filename in r_package_files:
        r_package_file = os.path.join(r_dir, filename)
        try:
            package = file_to_anonymous_package(r_package_file)
            sourced_r_packages[package.__rname__] = package
        except Exception as err:
            logger.warning("{}: {}".format(r_package_file, err))

    return sourced_r_packages
