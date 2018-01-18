// README.txt

Authors:        Christopher Negrich, Andrew Hoetker, Courtney Johnson
Contact:        cnegrich@gmail.com, ahoetker@me.com, cejohn32@asu.edu
Github:         cnegrich, ahoetker, cejohn32

Date Created:   September 27, 2017
Language Used:  Python 3.6
Packages Used:  Pandas (+xlrd), NumPy, NetworkX, SciPy, matplotlib, Rpy2, 

Basic pip commands for install:
  For Linux/Unix based Users:
    pip install pandas && pip install numpy && pip install networkx
      -This will automatically install scipy and numpy-mkl
  For Windows Users:
    Python Wheels: http://www.lfd.uci.edu/~gohlke/pythonlibs/
    .\python -m pip install "C:\..filepath..\scipy.whl"
    .\python -m pip install "C:\..filepath..\numpy-mkl.whl"
    .\python -m pip install "C:\..filepath..\networkx.whl"
    .\python -m pip install pandas
      Alternatively, Windows users may want to use anaconda as a package manager

Some Notes on Design Philosophy and Methods:
  For all analysis, the entire table provided is used. This will need to be
  parsed down to the desired values. All math is done pairwise by columns. Data
  is reformatted manually before analysis to allow for clean labels during import.
  This program was originally written with a tool framework but then changed to
  a more basic framework to allow for efficient analysis. The approach for the
  code framework is "quick and dirty" with accurate analysis. For more flexible
  functionality, the program could be converted to a general tool. Of the desired
  provided analysis list, all analysis that has low statistical value or is
  not applicable is omitted.

File Output Names and Corresponding Data Contained:
  Starting Name    :  Connected Analysis
  desc_stats_      :  Basic Descriptive Statistics
  std_corr_frame_  :  Pearson Correlation
  sprc_corr_frame_ :  Spearman Correlation
  ktc_corr_frame_  :  Kendall Tau Correlation
  cov_frame_       :  Standard Covariance
  wc_corr_adj_     :  Weighted Correlation Analysis (WGCNA) Adjacency Matrix
  ranked_frame_    :  Matrix Rank

    -Note: The other portions of the WCGNA may be exported to files separately

Usage Instructions:
  For this analysis:
    1. Make sure that python 2.7.XX is the default version of python
    2. Install dependencies
      pip install pandas && pip install numpy && pip install networkx
    3. Run: python microbiome_analysis_arctic.py

  For generalized Use (Recommended that code is prepared in new framework first):
    1. Clean excel sheets in similar manner to Prepared_Data.xlsx
    2. Change hardcoded names
    3. Carry changes forward throughout the main
    4. Implement any additional needed methods
    5. Run
      Basic Steps for Program Generalization:
        1. File I/O framework support
             Input support needed:   .xlsx, .csv, .tsv, .txt
             Output support neeeded: .xlsx, .csv, .tsv, .txt
        2. Create a main() function that governs a basic UI
        3. Optional analysis algorithms implemented
        4. Install script created to automatically install dependencies

Sources:
  Pandas API:
    http://pandas.pydata.org/pandas-docs/stable/api.html
  NumPy API:
    https://docs.scipy.org/doc/numpy/reference/
