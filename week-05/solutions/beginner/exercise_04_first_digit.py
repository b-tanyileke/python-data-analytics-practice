"""Exercise 4 sample solution."""


def first_digit(text):
    """Return the first digit in text or an empty string when none exists."""
    for character in text:
        if not character.isdigit():
            continue
        return character

    return ""
