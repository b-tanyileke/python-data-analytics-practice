"""Exercise 6 sample solution."""


def write_number_summary(input_filename, output_filename):
    """Write a summary of the whole numbers in input_filename."""
    input_file = open(input_filename, "r")
    total = 0
    count = 0
    smallest = None
    largest = None

    for line in input_file:
        number = int(line.strip())
        total += number
        count += 1

        if smallest is None or number < smallest:
            smallest = number
        if largest is None or number > largest:
            largest = number

    input_file.close()
    average = total / count

    output_file = open(output_filename, "w")
    output_file.write("Count: " + str(count) + "\n")
    output_file.write("Total: " + str(total) + "\n")
    output_file.write("Smallest: " + str(smallest) + "\n")
    output_file.write("Largest: " + str(largest) + "\n")
    output_file.write("Average: " + format(average, ".2f") + "\n")
    output_file.close()

    return average
