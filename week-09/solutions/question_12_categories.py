"""Question 12 sample solution."""
import pandas as pd


def high_score_report(frame):
    """Return passing scores and labels in ascending score order."""
    report = frame.copy()
    report["result"] = report["score"].apply(
        lambda score: "Pass" if score >= 60 else "Review"
    )
    report = report.loc[report["score"] >= 60, ["score", "result"]]
    return report.sort_values("score", kind="stable")
