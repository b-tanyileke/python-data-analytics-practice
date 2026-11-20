"""Maintenance tests for the Week 7 sample solutions."""

import importlib.util
import sys
from pathlib import Path

import numpy as np


SOLUTION_ROOT = Path(__file__).parents[1] / "solutions"


def load_solution(relative_path, module_name):
    """Load a sample solution module from the specified relative path."""
    module_path = SOLUTION_ROOT / relative_path
    specification = importlib.util.spec_from_file_location(module_name, module_path)
    if specification is None or specification.loader is None:
        raise ImportError(f"Unable to load solution module from {module_path}")
    module = importlib.util.module_from_spec(specification)
    sys.modules[module_name] = module
    specification.loader.exec_module(module)
    return module


def test_create_score_array():
    """Test the create_score_array function."""
    solution = load_solution("short-answer/question_13_create_array.py", "create_array_solution")
    result = solution.create_score_array([80, 92, 75])
    assert np.array_equal(result, np.array([80.0, 92.0, 75.0]))
    assert np.issubdtype(result.dtype, np.floating)


def test_center_block():
    """Test the center_block function."""
    solution = load_solution("short-answer/question_14_slice_matrix.py", "slice_solution")
    matrix = np.arange(1, 17).reshape(4, 4)
    assert np.array_equal(solution.center_block(matrix), np.array([[6, 7], [10, 11]]))


def test_replace_negatives():
    """Test replace_negatives without accepting a changed input array."""
    solution = load_solution("short-answer/question_15_replace_negatives.py", "replace_solution")
    values = np.array([4, -2, 0, -7, 3])
    assert np.array_equal(solution.replace_negatives(values), np.array([4, 0, 0, 0, 3]))
    assert np.array_equal(values, np.array([4, -2, 0, -7, 3]))


def test_row_totals():
    """Test the row_totals function."""
    solution = load_solution("short-answer/question_16_row_totals.py", "rows_solution")
    assert np.array_equal(solution.row_totals(np.array([[1, 2, 3], [4, 5, 6]])), np.array([6, 15]))


def test_transpose_and_scale():
    """Test the transpose_and_scale function."""
    solution = load_solution("short-answer/question_17_transpose_and_scale.py", "transpose_solution")
    matrix = np.array([[1, 2, 3], [4, 5, 6]])
    expected = np.array([[10, 40], [20, 50], [30, 60]])
    assert np.array_equal(solution.transpose_and_scale(matrix, 10), expected)


def test_random_binary_matrix():
    """Test the random_binary_matrix function."""
    solution = load_solution("short-answer/question_18_random_binary_matrix.py", "random_solution")
    expected = np.array([[1, 0, 1], [0, 1, 1]])
    assert np.array_equal(solution.random_binary_matrix(7), expected)
