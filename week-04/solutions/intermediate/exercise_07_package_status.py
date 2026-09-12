"""Exercise 7 sample solution."""


def package_status(destination, weight):
    if destination == "local":
        if weight <= 5:
            return "Local standard"
        return "Local heavy"

    if weight <= 2:
        return "International standard"
    return "International heavy"
