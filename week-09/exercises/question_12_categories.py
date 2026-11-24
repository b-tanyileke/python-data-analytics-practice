"""Question 12: Apply a function and select rows

Write a function named high_score_report accepting a DataFrame with unique
student names as its index and numeric columns "score" and "hours". Scores
are non-missing. Create a new column "result" by applying a function to each
score: use "Pass" for scores of 60 or higher and "Review" otherwise.

Return only rows with score at least 60, sorted by score in ascending order,
with columns "score" and "result" in that order. If scores tie, preserve the
original order of tied rows. Do not change the input DataFrame.

For example, for Ada: 75, Ben: 50, Chen: 60, the returned rows are:

      score result
Chen     60   Pass
Ada      75   Pass
"""

import pandas as pd


# Write your function below.
