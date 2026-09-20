# Week 5 Hints

Use one hint at a time. Try the exercise again after each hint before reading
the solution.

## Exercise 1: Running total

Start `total` at 0. Each time through the loop, add the current value to
`total`.

## Exercise 2: Sentinel counter

Use a variable such as `position` as both the current index and the count.
Continue while it is smaller than the length of the text. Stop with `break`
when the current character is `"*"`.

## Exercise 3: Count vowels

Loop through the characters. Convert each character to lowercase before
checking whether it is in the string `"aeiou"`.

## Exercise 4: Find the first digit

Use `character.isdigit()` to test each character. `continue` skips a
non-digit; returning a digit immediately ends the function.

## Exercise 5: Write a message to a file

Open the file in `"w"` mode. Add `"\n"` to the message that is written, but
use `len(message)` for the returned count.

## Exercise 6: Number-file summary

Convert each stripped line to an integer inside the loop. Update the total and
count for every number. Keep separate variables for the smallest and largest
values, and write the summary only after the input file has been read.

## Exercise 7: Mailbox line analysis

`line.startswith("From ")` is `True` only when the line begins with `From`
followed by a space. This does not match `From:`.

## Exercise 8: Multiplication-table file

The outer loop controls the row and the inner loop controls the column. Write
the newline after the inner loop completes.
