NUM_MEASUREMENTS = 3
sample_name = input("Sample name: ")
measurement_one = float(input("Measurement 1: "))
measurement_two = float(input("Measurement 2: "))
measurement_three = float(input("Measurement 3: "))
total = measurement_one + measurement_two + measurement_three
average = total / NUM_MEASUREMENTS
print("Sample: " + sample_name)
print("Total: " + format(total, ".2f"))
print("Average: " + format(average, ".2f"))
