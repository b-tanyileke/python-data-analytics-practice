"""Shared behavioral checks for Week 10 exercises and sample solutions."""

import importlib.util
from pathlib import Path

import pandas as pd
from pandas.testing import assert_frame_equal


def load(folder, filename):
    """Load a question module from the specified folder."""
    path = Path(__file__).parent / folder / filename
    spec = importlib.util.spec_from_file_location("week10_" + path.stem, path)
    if spec is None or spec.loader is None:
        raise ImportError(f"Cannot load {path}")
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def check_clean(folder):
    """Check cleanup order, missing names, and input preservation."""
    module = load(folder, "question_09_clean_records.py")
    frame = pd.DataFrame({"name": [" Ada ", "ada", "BEN", None], "score": [80, 90, None, 50]})
    original = frame.copy(deep=True)
    expected = pd.DataFrame({"name": ["ada", "ben"], "score": [80, 0]}, index=[0, 2])
    assert_frame_equal(module.clean_records(frame), expected, check_dtype=False)
    assert_frame_equal(frame, original)


def check_transform(folder):
    """Check replacement, mapping, and column labels."""
    module = load(folder, "question_10_transform.py")
    frame = pd.DataFrame({"dept": ["IT", "HR"], "hours": [8, "N/A"]}, index=[4, 7])
    original = frame.copy(deep=True)
    expected = pd.DataFrame({"department": ["Technology", "Human Resources"], "hours_worked": [8, float("nan")]}, index=[4, 7])
    assert_frame_equal(module.department_report(frame), expected, check_dtype=False)
    assert_frame_equal(frame, original)


def check_bands(folder):
    """Check band boundaries, absent bands, and unchanged inputs."""
    module = load(folder, "question_11_bins_dummies.py")
    frame = pd.DataFrame({"score": [0, 59, 60, 100]}, index=[2, 3, 4, 5])
    original = frame.copy(deep=True)
    expected = pd.DataFrame({"score": [0, 59, 60, 100], "Low": [1, 1, 0, 0], "High": [0, 0, 1, 1]}, index=frame.index)
    assert_frame_equal(module.score_bands(frame), expected, check_dtype=False)
    assert_frame_equal(frame, original)
    result = module.score_bands(pd.DataFrame({"score": [10]}))
    assert list(result.columns) == ["score", "Low", "High"]
    assert result.loc[0, "High"] == 0


def check_sample(folder):
    """Check complete-row filtering, duplicate order, and sampling."""
    module = load(folder, "question_12_sample.py")
    frame = pd.DataFrame({"name": ["Ada", "Ada", "Ben", "Chen"], "score": [80, 90, 70, None]})
    original = frame.copy(deep=True)
    expected = frame.loc[[2, 0], ["name", "score"]]
    assert_frame_equal(module.sample_complete_records(frame, 2), expected)
    assert len(module.sample_complete_records(frame, 0)) == 0
    assert_frame_equal(frame, original)
