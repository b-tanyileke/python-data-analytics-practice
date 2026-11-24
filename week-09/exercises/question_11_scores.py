"""Question 11: Prepare a score report

Write a function named score_report accepting a DataFrame with unique student
names as its index and numeric columns "score" and "hours". Assume scores
are non-missing and distinct. Return a new DataFrame with columns "score",
"adjusted", and "rank", in that order. The adjusted score is score + 5;
rank is based on adjusted score, with 1 for the highest score. Sort rows by
adjusted score, highest first. Do not change the input DataFrame.

For example, if Ada has score 80 and Ben has score 90, the returned rows are:

       score  adjusted  rank
Ben       90        95   1.0
Ada       80        85   2.0
"""

import pandas as pd


# Write your function below.
