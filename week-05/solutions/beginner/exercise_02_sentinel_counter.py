"""Exercise 2 sample solution."""


def count_before_stop(text):
    """Return the number of characters before the first asterisk."""
    position = 0

    while position < len(text):
        if text[position] == "*":
            break
        position += 1

    return position
