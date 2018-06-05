"""
analyze.py
This module exists to provide doConstrictPy to the webapp.
It is a modified form of constrictpy/microbiome_analysis_arctic.py

"""
# Import all needed packages, see documentation for details
import pandas as pd

# Import custom modules and classes
from constrictpy.Dataset import Dataset  # Dataset classes
from constrictpy.std_corr import StdCorr, SprCorr, KtCorr  # Correlation functions
from constrictpy.std_stats import (  # Descriptive stats, ranking, covariance functions
    StdDescStats,
    StdDataRanking,
    StdCov,
)
from constrictpy.wgcna import WGCNA  # Weighted Correlation Network Analysis
from constrictpy.io_handling import ensureDir, batchSaveToFile, compressDir, moveToUploads
from constrictpy.rfunctions import sourceRFunctions, rFunc
import logging
from constrictpy.logger import startLogger

"""
Main function
"""


def doConstrictPy(datafile, use_methods):

    """
    Define Constants
    """
    OUTPUT_DIR = "output-files/"  # Define the output directory
    CSV_DIR = OUTPUT_DIR + "csv/"  # Define the CSV data directory
    R_DIR = OUTPUT_DIR + "r-data-objects/"  # Define the R data directory
    CLEAR_OUTPUT = True  # Clear output directories before saving files
    LOG_LEVEL = "info"
    CLEAR_LOG = True

    """
    Start logging. The logger module is found in constrictpy/logging.py
    """
    startLogger(LOG_LEVEL, CLEAR_LOG)
    logging.info("Starting")

    """
    Data Import
    Parse sheets of the excel data into six Dataset objects as dataset.source
    In this version, analyze.py is only intended to handle the data included
    with the package, 'Prepared_Data.xlsx'
    """
    # Excel file
    excel_file = pd.ExcelFile(datafile)

    # Import excel sheets
    sheet_2014 = Dataset("sheet_2014", excel_file.parse("sample_conditions_year_2014"))
    sheet_2016 = Dataset("sheet_2016", excel_file.parse("sample_conditions_year_2016"))
    sheet_OTU_abundance = Dataset(
        "sheet_OTU_abundance", excel_file.parse("Sorted_OTU_Abundance")
    )
    sheet_2016_2014 = Dataset(
        "sheet_2016_2014", excel_file.parse("sample_conditions_2016_2014")
    )
    sheet_16S_2014_OTU = Dataset("sheet_16S_2014_OTU", excel_file.parse("16S_2014_OTU"))
    sheet_16S_2016_OTU = Dataset("sheet_16S_2016_OTU", excel_file.parse("16S_2016_OTU"))
    sheet_combined_14 = Dataset("sheet_combined_14", excel_file.parse("combined_14"))
    sheet_combined_16 = Dataset("sheet_combined_16", excel_file.parse("combined_16"))



    """
    Rpy2 Spinup
    Start the Rpy2 instance and source functions from ConstrictR
    """
    sourceRFunctions()

    """
    Descriptive statistics, Ranking, WGCNA, Covariance for each sheet
    Dataframes are added to Dataset objects
    """
    # Create an array of imported sheets
    initial_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_OTU_abundance,
        sheet_2016_2014,
        sheet_16S_2014_OTU,
        sheet_16S_2016_OTU,
        sheet_combined_14,
        sheet_combined_16,
    ]

    # Run basic statistical analysis over all sheets in initial_dataset list
    logging.info(
        "Calculating Descriptive Statistics, Ranking, WGCNA, and Covariance..."
    )

    for ds in initial_datasets:
        logging.info(f"\tAnalysis of {ds.name}...")
        if use_methods["std_desc_stats"] is True:
            ds.addStats("std_desc_stats", rFunc("desc_stats", ds.source))
        if use_methods["std_data_ranking"] is True:
            ds.addStats("std_data_ranking", StdDataRanking(ds.source))
        if use_methods["WGCNA"] is True:
            ds.addStats("WGCNA", WGCNA(ds.source))
        if use_methods["std_cov"] is True:
            ds.addStats("std_cov", StdCov(ds.source))

    """
    Correlation Analysis
    For each sheet of data, runs four centrality analyses. Each analysis
    is done columnwise across the dataframe.
    """

    # Equivalent to initial_datasets, copy made for ease of analysis change
    corr_datasets = [
        sheet_2014,
        sheet_2016,
        sheet_OTU_abundance,
        sheet_2016_2014,
        sheet_16S_2014_OTU,
        sheet_16S_2016_OTU,
    ]

    # List of correlation functions to be run
    corr_functions = {"std_corr": StdCorr, "spr_corr": SprCorr, "kt_corr": KtCorr}


    # Run the correlation functions in corr_functions on the corr_datasets
    logging.info("Calculating Correlation...")
    for ds in corr_datasets:
        logging.info(f"\tAnalysis of {ds.name}...")
        for cf in corr_functions:
            if use_methods[cf] is True:
                ds.addStats("%s" % (cf), corr_functions[cf](ds.source))

    """
    Combined Analysis
    This is for analysis of tables that combine both the OTU and viarable
    tables. These tables are simply the transpose of the variable and OTU
    datasets combined and re-indexed. This allows for a cross table analysis.
    """

    # List of the combined datasets
    combined_datasets = [sheet_combined_14, sheet_combined_16]

    # Functions that can be run on the combined datasets
    combined_functions = {
        "std_desc_stats": StdDescStats,
        "std_data_ranking": StdDataRanking,
        "WGCNA": WGCNA,
        "std_cov": StdCov,
        "std_corr": StdCorr,
        "spr_corr": SprCorr,
        "kt_corr": KtCorr,
    }

    # Run the combined functions on the combined datasets
    logging.info("Calculating Combined Analysis...")
    for ds in combined_datasets:
        logging.info(f"\tAnalysis of {ds.name}...")
        for cf in combined_functions:
            if use_methods[cf] is True:
                ds.addStats(cf, combined_functions[cf](ds.source))

    """
    Output

    Print lots of stuff to console if VERBOSE
    Make sure directories exist
    Save DataFrames to CSV files
    Save Dataframes to Rdata files
    """

    # Make sure the output directory exists
    ensureDir(OUTPUT_DIR)

    # CSV stuff
    ensureDir(CSV_DIR)
    batchSaveToFile(CSV_DIR, initial_datasets, "csv", clear=CLEAR_OUTPUT)

    # R stuff
    ensureDir(R_DIR)
    batchSaveToFile(R_DIR, initial_datasets, "Rdata", clear=CLEAR_OUTPUT)

    # archive the output
    compressDir(OUTPUT_DIR + "/archive", OUTPUT_DIR)
    moveToUploads(OUTPUT_DIR + "/archive.zip")
# Initiate the main function and prevent the others from running without being
# called
if __name__ == "__main__":
    doConstrictPy()
