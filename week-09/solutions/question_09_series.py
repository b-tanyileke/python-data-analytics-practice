"""Question 9 sample solution."""
import pandas as pd


def prepare_scores(scores):
    """Return adjusted scores in the specified index order."""
    return (pd.Series(scores, dtype=float) + 5).reindex(["Ada", "Ben", "Chen"])
