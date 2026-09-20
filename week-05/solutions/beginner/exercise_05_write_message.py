"""Exercise 5 sample solution."""


def write_message(message, filename):
    """Write message and a newline to filename, then return its length."""
    with open(filename, "w") as output_file:
        output_file.write(message + "\n")
    return len(message)
