import pytest
import pandas as pd
from constrictpy import rfunctions

"""
In its current state, this module tests imported R functions using a new
pandas DataFrame with some numbers. As R functions are implemented, these
tests will be conducted using the 'Prepared_Data.xlsx' data file.
"""

# source R functions into Rpy2
rfunctions.sourceRFunctions()


def test_desc_stats():
    # set up test environment
    data = [1, 1, 2, 3, 5, 8, 13]
    df = pd.DataFrame(data)
    result = rfunctions.rFunc("desc_stats", df)

    assert result["mean"][0] == 4.714285714285714
    assert result["var"][1] == 19.571428571428573
    assert result["sd"][0] == 4.423960733486292
    assert result["se"][1] == 1.6720999872456608


