"""Question 12 sample solution."""
import pandas as pd


def sample_complete_records(frame, sample_size):
    """Return a reproducible sample of complete, unique-name records."""
    records = frame.loc[:, ["name", "score"]].dropna(subset=["name", "score"])
    records = records.drop_duplicates(subset=["name"], keep="first")
    return records.sample(n=sample_size, random_state=42)
