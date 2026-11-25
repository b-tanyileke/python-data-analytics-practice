"""Question 9 sample solution."""
import pandas as pd


def clean_records(frame):
    """Clean names, remove duplicates, and fill missing scores."""
    result = frame.loc[:, ["name", "score"]].copy()
    result["name"] = result["name"].str.strip().str.lower()
    result = result.dropna(subset=["name"]).drop_duplicates(subset=["name"])
    result["score"] = result["score"].fillna(0)
    return result
