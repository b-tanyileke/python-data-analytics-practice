"""Question 18 sample solution."""

import numpy as np


def random_binary_matrix(seed):
    """Return a repeatable 2-by-3 matrix of pseudorandom zeros and ones."""
    np.random.seed(seed)
    return np.random.randint(0, 2, size=(2, 3))
