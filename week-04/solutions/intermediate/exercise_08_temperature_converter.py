"""Exercise 8 sample solution."""

import conversion_tools


def convert_temperature(temperature, scale):
    if scale == "C":
        return conversion_tools.celsius_to_fahrenheit(temperature)
    if scale == "F":
        return conversion_tools.fahrenheit_to_celsius(temperature)
    return "Invalid scale"
