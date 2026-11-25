"""Question 11: Create score bands and indicators

Write a function called score_bands accepting a DataFrame containing a
non-missing numeric "score" column. All scores are between 0 and 100,
inclusive. Return a new DataFrame with the original "score" column followed
by integer indicator columns "Low" and "High", in that order. Low means a
score from 0 through 59, and High means a score from 60 through 100.
Each row must have a 1 in its band and 0 in the other. Include both indicator
columns even when one band is absent. Preserve the input index and do not
modify the input.

Use `pd.cut` to create the bands and `pd.get_dummies` to create indicators.
For scores [0, 59, 60, 100], Low is [1, 1, 0, 0] and High is [0, 0, 1, 1].
"""

import pandas as pd


# Write your function below.
