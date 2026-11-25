"""Question 11 sample solution."""
import pandas as pd


def score_bands(frame):
    """Return scores with Low and High indicator columns."""
    bands = pd.cut(frame["score"], bins=[0, 60, 101], labels=["Low", "High"], right=False)
    indicators = pd.get_dummies(bands, dtype=int)
    return pd.concat([frame.loc[:, ["score"]], indicators.loc[:, ["Low", "High"]]], axis=1)
