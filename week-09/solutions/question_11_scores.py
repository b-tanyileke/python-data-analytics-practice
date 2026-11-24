"""Question 11 sample solution."""
import pandas as pd


def score_report(frame):
    """Return adjusted scores and descending ranks."""
    report = frame.loc[:, ["score"]].copy()
    report["adjusted"] = report["score"] + 5
    report["rank"] = report["adjusted"].rank(ascending=False)
    return report.sort_values("adjusted", ascending=False)
