"""Question 16 sample solution."""

import numpy as np


def row_totals(matrix):
    """Return a NumPy array containing the total of each matrix row."""
    return matrix.sum(axis=1)
