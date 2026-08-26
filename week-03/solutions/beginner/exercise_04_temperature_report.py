""" Exercise 04 - Sample Solution """

FAHRENHEIT_MULTIPLIER = 9 / 5
FAHRENHEIT_OFFSET = 32
celsius = float(input("Temperature in Celsius: "))
fahrenheit = celsius * FAHRENHEIT_MULTIPLIER + FAHRENHEIT_OFFSET
print("Temperature in Fahrenheit: " + format(fahrenheit, ".1f"))
