"""Question 14 sample solution."""

import numpy as np


def center_block(matrix):
    """Return the center 2-by-2 block from a 4-by-4 matrix."""
    return matrix[1:3, 1:3]
