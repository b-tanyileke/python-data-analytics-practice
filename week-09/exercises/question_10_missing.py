"""Question 10: Identify missing data

Write a function named missing_by_column accepting a DataFrame. Select only
the columns "score" and "hours", in that order. Return a Series containing
the number of missing values in each selected column. Do not modify the input.

For example, for score [80, None, 90] and hours [None, 4, None], return a
Series with index ["score", "hours"] and values [1, 2].
"""

import pandas as pd


# Write your function below.
