# Week 6 Hints

Use one hint at a time. Try the exercise again after each hint before reading
the solution.

## Exercise 1: List average

`sum(numbers)` calculates the total of the list, and `len(numbers)` gives the
number of values. Divide one by the other.

## Exercise 2: Copy and add

Call `items.copy()` before changing anything. Use `not in` to check whether
the new value is already present, then use `append()` when it is not.

## Exercise 3: Word counts

Start with an empty dictionary. If a word is already a dictionary key, add 1
to its value. Otherwise, store 1 for that word.

## Exercise 4: Format a coordinate

Unpack the tuple with one assignment such as `x_coordinate, y_coordinate =
coordinate`. Convert each value to a string before joining it with text.

## Exercise 5: Read names into a list

Start with an empty list. Read one line at a time inside `with open(...)`.
Use `strip()` before deciding whether the name is blank.

## Exercise 6: Score summary

Keep variables for the highest name, highest score, and running total. Loop
through the dictionary keys, then use each key to look up its score.

## Exercise 7: Update inventory

Use `inventory.copy()` first. Loop through the sales dictionary and subtract
each sale quantity from the matching item in the copied dictionary.

## Exercise 8: 2D-list row totals

The outer loop selects one row. Start a new `row_total` at 0 for that row, and
use the inner loop to add its values before appending the total to the result.
