"""Question 15 sample solution."""

import numpy as np


def replace_negatives(values):
    """Return a copy of values with negative entries replaced by zero."""
    updated_values = values.copy()
    updated_values[updated_values < 0] = 0
    return updated_values
