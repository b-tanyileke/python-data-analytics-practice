"""Exercise 3 sample solution."""


def grade_label(score):
    """ returns a string based on the score """
    if score >= 90:
        return "A"
    if score >= 80:
        return "B"
    if score >= 70:
        return "C"
    return "Needs improvement"
