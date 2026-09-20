"""Exercise 3 sample solution."""


def count_vowels(text):
    """Return the number of vowels in text."""
    vowel_count = 0

    for character in text:
        if character.lower() not in "aeiou":
            continue
        vowel_count += 1

    return vowel_count
