"""Exercise 4 sample solution."""


def divide_numbers(numerator, denominator):
    try:
        return numerator / denominator
    except ZeroDivisionError:
        return "Cannot divide by zero."
