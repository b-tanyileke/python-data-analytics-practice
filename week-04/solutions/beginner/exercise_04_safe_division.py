"""Exercise 4 sample solution."""


def divide_numbers(numerator, denominator):
    """ returns the result of numerator divided by denominator """
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Cannot divide by zero."
