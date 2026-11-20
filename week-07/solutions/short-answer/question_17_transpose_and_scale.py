"""Question 17 sample solution."""

import numpy as np


def transpose_and_scale(matrix, factor):
    """Return the transposed matrix after elementwise scaling."""
    return matrix.T * factor
