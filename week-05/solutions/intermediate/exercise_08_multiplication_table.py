"""Exercise 8 sample solution."""


def write_multiplication_table(size, filename):
    """Write a size-by-size multiplication table to filename."""
    output_file = open(filename, "w")

    for row in range(1, size + 1):
        for column in range(1, size + 1):
            output_file.write(str(row * column) + " ")
        output_file.write("\n")

    output_file.close()
    return size * size
