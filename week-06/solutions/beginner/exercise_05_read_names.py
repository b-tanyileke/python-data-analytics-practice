"""Exercise 5 sample solution."""


def read_names(filename):
    """Return the non-blank names in filename as a list."""
    names = []

    with open(filename, "r") as input_file:
        for line in input_file:
            name = line.strip()
            if name != "":
                names.append(name)

    return names
