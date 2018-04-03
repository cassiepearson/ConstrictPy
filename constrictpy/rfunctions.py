"""
Created on Fri Mar 16 17:37:51 2018

@author: andrew

This file sources the given .R files to the RPy 2 engine.
For absolute ease of use, it should live in the ConstrictR directory
with the .R files.
"""

import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri
import os
import pkg_resources


def sourceRFunctions():
    """
    Source .R files from ConstrictR into the RPy2 engine.
    """
    pandas2ri.activate()

    constrict_r_dir = pkg_resources.resource_filename('constrictpy','ConstrictR')
    blacklist = ["centrality.R"]

    for file in os.listdir(constrict_r_dir):
        if os.path.splitext(file)[1] == '.R' and file not in blacklist:
            rfile = os.path.join(constrict_r_dir, file)
            r["source"](rfile)

def rFunc(r_function_name, df):
    r_df = r[f"{r_function_name}"](df)
    return pandas2ri.ri2py_dataframe(r_df)
