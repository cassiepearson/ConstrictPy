// README.txt

ConstrictPy

  _____            _               _   _____
 / ____|          | |      ( )    | | |  __ \
| |     ___  _ __ | |_ _ __ _  ___| |_| |__) |   _
| |    / _ \| '_ \| __| '__| |/ __| __|  ___/ | | |
| |___| (_) | | | | |_| |  | | (__| |_| |   | |_| |
 \_____\___/|_| |_|\__|_|  |_|\___|\__|_|    \__, |
                                              __/ |
                                             |___/


Authors:        Christopher Negrich, Andrew Hoetker, Courtney Johnson
Contact:        cnegrich@gmail.com, ahoetker@me.com, cejohn32@asu.edu
Github:         cnegrich, ahoetker, cejohn32

Date Created:   September 27, 2017
Language Used:  Python 3.6
Packages Used:  Pandas (+xlrd), NumPy, NetworkX, SciPy, matplotlib, Rpy2 

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

Original Philosophy:
  For all analysis, the entire table provided is used. This will need to be
  parsed down to the desired values. All math is done pairwise by columns. Data
  is reformatted manually before analysis to allow for clean labels during import.
  This program was originally written with a tool framework but then changed to
  a more basic framework to allow for efficient analysis. The approach for the
  code framework is "quick and dirty" with accurate analysis. For more flexible
  functionality, the program could be converted to a general tool. Of the desired
  provided analysis list, all analysis that has low statistical value or is
  not applicable is omitted.

Current Philosophy:
  This project has expanded to make the set of methods original implemented here more
  efficient, accurate, and usable. From the original program, we have expanded the
  python tool to include more methods and a much more robust object-oriented framework.
  Additionally, now the python portion is a tool wrapper for the analysis in R. The
  analysis in R has become a project and package of its own. The project is still a 
  work in progress and is expanding rapidly. Current plans involve the full project
  being available in July 2018.

Usage Instructions:
  For this analysis:
    1. Make sure that python 3.6.XX is the default version of python
    2. Install dependencies
      pip install pandas && pip install numpy && pip install networkx
    3. Run: python microbiome_analysis_arctic.py

Sources:
  Pandas API:
    http://pandas.pydata.org/pandas-docs/stable/api.html
  NumPy API:
    https://docs.scipy.org/doc/numpy/reference/
