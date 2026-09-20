"""Exercise 7 sample solution."""


def count_sender_lines(filename):
    """Return the number of mailbox lines that begin with From and a space."""
    with open(filename, "r") as input_file:
        sender_count = 0

        for line in input_file:
            if line.startswith("From "):
                sender_count += 1

        return sender_count
