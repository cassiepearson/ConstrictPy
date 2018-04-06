"""
Initialize the R portion of the program by activating pandas2ri
and sourcing the functions from ConstrictR.
"""

import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri
import os
import pkg_resources


def sourceRFunctions():
    """
    Source .R files from ConstrictR into the RPy2 engine.
    Should be called near the top of main program. 
    """
    pandas2ri.activate()

    r_dir = pkg_resources.resource_filename('ConstrictR','')
    blacklist = []

    for file in os.listdir(r_dir):
        if os.path.splitext(file)[1] == '.R' and file not in blacklist:
            rfile = os.path.join(r_dir, file)
            r["source"](rfile)


def rFunc(r_function_name, df):
    """
    Passes the string r_function_name and the DataFrame df to Rpy2. 
    Returns the DataFrame from R once converted back to pandas DataFrame.
    """
    r_df = r[f"{r_function_name}"](df)
    return pandas2ri.ri2py_dataframe(r_df)
    
