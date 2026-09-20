"""Exercise 6 sample solution."""


def write_number_summary(input_filename, output_filename):
    """Write a summary of the whole numbers in input_filename."""
    total = 0
    count = 0
    smallest = None
    largest = None

    with open(input_filename, "r") as input_file:
        for line in input_file:
            number = int(line.strip())
            total += number
            count += 1

            if smallest is None or number < smallest:
                smallest = number
            if largest is None or number > largest:
                largest = number

    if count == 0:
        raise ValueError(f"No numbers found in {input_filename}")

    average = total / count

    output_file = open(output_filename, "w")
    output_file.write("Count: " + str(count) + "\n")
    output_file.write("Total: " + str(total) + "\n")
    output_file.write("Smallest: " + str(smallest) + "\n")
    output_file.write("Largest: " + str(largest) + "\n")
    output_file.write("Average: " + format(average, ".2f") + "\n")
    output_file.close()

    return average
