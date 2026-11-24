"""Question 9: Series selection and reindexing

Write a function named prepare_scores accepting a dictionary mapping student
names to numeric scores. Create a pandas Series from it, add 5 to every score,
and reindex the result in this order: Ada, Ben, Chen. Return the Series.
Missing names must have pandas missing values; do not fill them.

For example, prepare_scores({"Ben": 70, "Ada": 80}) returns a Series with
index ["Ada", "Ben", "Chen"] and values [85, 75, NaN].
"""

import pandas as pd


# Write your function below.
