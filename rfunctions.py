#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Mar 16 17:37:51 2018

@author: andrew
"""

import rpy2.robjects as robjects
from rpy2.robjects import r, pandas2ri

pandas2ri.activate()

# Source R functions from files into 
rfunctions = ["desc_stats.R"]
for rfunction in rfunctions:
    r["source"](rfunction)

def rFunc(r_function_name, df):
    r_df = r[f"{r_function_name}"](df)
    return pandas2ri.ri2py_dataframe(r_df)