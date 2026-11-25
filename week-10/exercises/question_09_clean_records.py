"""Question 9: Clean student records

Write a function called clean_records that accepts a DataFrame with columns
"name" and "score". Make a copy, strip leading and trailing whitespace from
names, and convert names to lowercase. Remove rows with missing names, then
remove duplicate cleaned names, keeping the first row. Replace missing scores
in the remaining rows with 0. Return these two columns in their original order,
preserving the surviving row indexes. Do not modify the input.

For example, rows indexed 0, 1, 2 with names [" Ada ", "ada", "BEN"] and
scores [80, 90, None] produce rows indexed 0, 2 with names ["ada", "ben"]
and scores [80, 0].
"""

import pandas as pd


# Write your function below.
