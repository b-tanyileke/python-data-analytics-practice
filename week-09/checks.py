"""Shared behavioral checks for Week 9 exercises and sample solutions."""

import importlib.util
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal, assert_series_equal


def load(folder, filename):
    """Load a question from the selected folder."""
    path = Path(__file__).parent / folder / filename
    spec = importlib.util.spec_from_file_location("week09_" + path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_series(folder):
    """Check reindexing, arithmetic, and missing labels."""
    module = load(folder, "question_09_series.py")
    expected = pd.Series([85.0, 75.0, float("nan")], index=["Ada", "Ben", "Chen"])
    assert_series_equal(module.prepare_scores({"Ben": 70, "Ada": 80}), expected, check_dtype=False)


def check_missing(folder):
    """Check selected-column missing counts."""
    module = load(folder, "question_10_missing.py")
    frame = pd.DataFrame({"score": [80, None, 90], "hours": [None, 4, None], "other": [None] * 3})
    original = frame.copy(deep=True)
    assert_series_equal(module.missing_by_column(frame), pd.Series([1, 2], index=["score", "hours"]))
    assert_frame_equal(frame, original)


def check_scores(folder):
    """Check adjusted scores, rank, order, and input preservation."""
    module = load(folder, "question_11_scores.py")
    frame = pd.DataFrame({"score": [80, 90], "hours": [4, 3]}, index=["Ada", "Ben"])
    original = frame.copy(deep=True)
    expected = pd.DataFrame({"score": [90, 80], "adjusted": [95, 85], "rank": [1.0, 2.0]}, index=["Ben", "Ada"])
    assert_frame_equal(module.score_report(frame), expected, check_dtype=False)
    assert_frame_equal(frame, original)


def check_categories(folder):
    """Check filtering, boundary, tie order, and input preservation."""
    module = load(folder, "question_12_categories.py")
    frame = pd.DataFrame({"score": [75, 50, 60, 60], "hours": [1, 2, 3, 4]}, index=["Ada", "Ben", "Chen", "Dia"])
    original = frame.copy(deep=True)
    expected = pd.DataFrame({"score": [60, 60, 75], "result": ["Pass"] * 3}, index=["Chen", "Dia", "Ada"])
    assert_frame_equal(module.high_score_report(frame), expected)
    assert_frame_equal(frame, original)
