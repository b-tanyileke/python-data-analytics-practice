"""Question 10: Standardize a department report

Write a function called department_report accepting a DataFrame with columns
"dept" and "hours". Replace "N/A" in hours with a missing value. The other
hours values are numbers. Map department codes "IT" to "Technology" and
"HR" to "Human Resources"; assume these are the only department codes.
Rename the columns to "department" and "hours_worked", in that order.
Return the new DataFrame with its original index. Do not modify the input.

For example, dept ["IT", "HR"] and hours [8, "N/A"] produce department
["Technology", "Human Resources"] and hours_worked [8, NaN].
"""

import pandas as pd


# Write your function below.
