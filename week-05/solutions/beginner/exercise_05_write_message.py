"""Exercise 5 sample solution."""


def write_message(message, filename):
    """Write message and a newline to filename, then return its length."""
    output_file = open(filename, "w")
    output_file.write(message + "\n")
    output_file.close()
    return len(message)
