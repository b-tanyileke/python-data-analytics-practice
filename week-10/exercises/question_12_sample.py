"""Question 12: Clean and sample a dataset

Write a function called sample_complete_records accepting a DataFrame with
columns "name" and "score", and an integer named sample_size. First remove
rows with a missing name or score. Then remove duplicate names, keeping the
first complete row. Select exactly sample_size rows without replacement using
`random_state=42`. Return the sampled rows in the order returned by `sample`,
with columns "name" and "score" and their original indexes.

Assume sample_size is between 0 and the number of remaining rows, inclusive.
Do not modify the input DataFrame.

For example, for rows 0–3 containing ("Ada", 80), ("Ada", 90), ("Ben", 70),
and ("Chen", None), sample_size 2 selects the complete first Ada and Ben
rows, indexed 2 and 0, in that order when using pandas `random_state=42`.
"""

import pandas as pd


# Write your function below.
