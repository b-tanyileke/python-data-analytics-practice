"""Exercise 1 sample solution."""


def number_category(number):
    if number > 0:
        return "positive"
    if number < 0:
        return "negative"
    return "zero"
