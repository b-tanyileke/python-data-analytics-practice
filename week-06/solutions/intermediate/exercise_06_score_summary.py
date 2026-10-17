"""Exercise 6 sample solution."""


def score_summary(scores):
    """Return the highest-scoring name and the average score as a tuple."""
    highest_name = ""
    highest_score = None
    total = 0

    for name in scores:
        score = scores[name]
        total += score

        if highest_score is None or score > highest_score:
            highest_name = name
            highest_score = score

    average = total / len(scores)
    return highest_name, average
