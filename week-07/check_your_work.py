"""Optional self-checks for the Week 7 starter exercises.

Run from the repository root with:
python -m pytest week-07/check_your_work.py
"""

import importlib.util
import sys
from pathlib import Path

import numpy as np


EXERCISE_ROOT = Path(__file__).parent / "exercises"


def load_exercise(relative_path, module_name):
    """Load a student exercise file so its functions can be checked."""
    module_path = EXERCISE_ROOT / relative_path
    specification = importlib.util.spec_from_file_location(module_name, module_path)
    if specification is None or specification.loader is None:
        raise ImportError(f"Unable to load exercise module from {module_path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


def test_create_score_array():
    """Check the create_score_array function."""
    exercise = load_exercise("short-answer/question_13_create_array.py", "student_create_array")
    result = exercise.create_score_array([80, 92, 75])
    assert np.array_equal(result, np.array([80.0, 92.0, 75.0]))
    assert np.issubdtype(result.dtype, np.floating)


def test_center_block():
    """Check the center_block function."""
    exercise = load_exercise("short-answer/question_14_slice_matrix.py", "student_slice")
    matrix = np.arange(1, 17).reshape(4, 4)
    assert np.array_equal(exercise.center_block(matrix), np.array([[6, 7], [10, 11]]))


def test_replace_negatives():
    """Check replace_negatives without accepting a changed input array."""
    exercise = load_exercise("short-answer/question_15_replace_negatives.py", "student_replace")
    values = np.array([4, -2, 0, -7, 3])
    assert np.array_equal(exercise.replace_negatives(values), np.array([4, 0, 0, 0, 3]))
    assert np.array_equal(values, np.array([4, -2, 0, -7, 3]))


def test_row_totals():
    """Check the row_totals function."""
    exercise = load_exercise("short-answer/question_16_row_totals.py", "student_rows")
    assert np.array_equal(exercise.row_totals(np.array([[1, 2, 3], [4, 5, 6]])), np.array([6, 15]))


def test_transpose_and_scale():
    """Check the transpose_and_scale function."""
    exercise = load_exercise("short-answer/question_17_transpose_and_scale.py", "student_transpose")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    expected = np.array([[10, 40], [20, 50], [30, 60]])
    assert np.array_equal(exercise.transpose_and_scale(matrix, 10), expected)


def test_random_binary_matrix():
    """Check the random_binary_matrix function."""
    exercise = load_exercise("short-answer/question_18_random_binary_matrix.py", "student_random")
    expected = np.array([[1, 0, 1], [0, 1, 1]])
    assert np.array_equal(exercise.random_binary_matrix(7), expected)
