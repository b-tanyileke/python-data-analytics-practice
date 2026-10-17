"""Exercise 3 sample solution."""


def count_words(words):
    """Return a dictionary containing the count of each word."""
    word_counts = {}

    for word in words:
        if word in word_counts:
            word_counts[word] += 1
        else:
            word_counts[word] = 1

    return word_counts
