# Think About It

Answer the questions before checking `solutions/think-about-it-answers.md`.

## Predict the output

1. What is displayed?

   ```python
   total = 0

   for number in range(1, 4):
       total += number

   print(total)
   ```

2. What is displayed?

   ```python
   text = "data*analysis"
   position = 0

   while text[position] != "*":
       position += 1

   print(position)
   ```

3. What is displayed?

   ```python
   word = "Python"

   for character in word:
       if character == "h":
           continue
       print(character, end="")
   ```

4. What is displayed?

   ```python
   for number in range(1, 6):
       if number == 4:
           break
       print(number, end=" ")
   ```

5. What is displayed?

   ```python
   course = "CS5302"
   print(course[2:5])
   ```

## Multiple choice

6. Which statement repeats its block while a condition is `True`?

   - A. `if`
   - B. `while`
   - C. `def`
   - D. `return`

7. Which statement immediately ends the nearest loop?

   - A. `break`
   - B. `continue`
   - C. `pass`
   - D. `close`

8. A running total should normally be initialized to:

   - A. `0`
   - B. `1`
   - C. `"total"`
   - D. `None`

9. Which string method returns `True` when every character is a digit?

   - A. `isalpha()`
   - B. `isdigit()`
   - C. `upper()`
   - D. `strip()`

10. Which file mode opens a file for writing and replaces its previous
    contents?

    - A. `"r"`
    - B. `"w"`
    - C. `"a"`
    - D. `"x"`

11. Which expression identifies a line that begins with `From `?

    - A. `line.endswith("From ")`
    - B. `line.startswith("From ")`
    - C. `line.isdigit("From ")`
    - D. `line.strip("From ")`

## Find and fix the problem

12. This code should add the values from 1 through 5. Correct the `range`.

    ```python
    total = 0

    for number in range(1, 5):
        total += number

    print(total)
    ```

13. This code should stop the loop when `letter` is `"x"`. Correct the
    statement inside the `if` block.

    ```python
    for letter in "example":
        if letter == "x":
            continue
        print(letter)
    ```

14. This code should write `Hello` to `message.txt`. Correct the file mode.

    ```python
    output_file = open("message.txt", "r")
    output_file.write("Hello")
    output_file.close()
    ```
