"""Question 10 sample solution."""
import pandas as pd


def missing_by_column(frame):
    """Count missing values in the two requested columns."""
    return frame.loc[:, ["score", "hours"]].isna().sum()
