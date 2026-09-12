# Week 4 Hints

Use one hint at a time. Try the exercise again after each hint before reading
the solution.

## Exercise 1: Number category

Check whether the number is greater than 0 first, then less than 0. If neither
condition is true, the number must be 0.

## Exercise 2: Admission check

The two requirements must both be true. Compare the ticket response directly
with the text `"yes"` and join the two checks with `and`.

## Exercise 3: Grade label

Check the highest score range first. Once a score is not at least 90, checking
whether it is at least 80 is enough to identify the B range.

## Exercise 4: Safe division

Put the division operation inside a `try` block. A denominator of 0 raises
`ZeroDivisionError`, which can be handled in an `except` block.

## Exercise 5: Distance to the origin

Import `math` at the top of the file. The expression inside `math.sqrt()` is
the square of x plus the square of y.

## Exercise 6: Member order total

Calculate the subtotal before writing the conditional. The discount applies
only if both the membership response and subtotal condition are true.

## Exercise 7: Package status

Start by checking the destination. Inside each destination case, compare the
weight with that destination's limit.

## Exercise 8: Temperature-converter module

Keep the conversion formulas in `conversion_tools.py`. In the converter file,
import that module and call its functions with dot notation, such as
`conversion_tools.celsius_to_fahrenheit(temperature)`.
