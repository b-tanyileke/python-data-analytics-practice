"""Exercise 1 sample solution."""


def sum_to_number(number):
    """Return the total of the whole numbers from 1 through number."""
    total = 0
    for value in range(1, number + 1):
        total += value
    return total
