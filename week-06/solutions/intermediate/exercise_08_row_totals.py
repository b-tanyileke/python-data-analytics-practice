"""Exercise 8 sample solution."""


def row_totals(matrix):
    """Return a list containing the total of every row in matrix."""
    totals = []

    for row in matrix:
        row_total = 0
        for value in row:
            row_total += value
        totals.append(row_total)

    return totals
