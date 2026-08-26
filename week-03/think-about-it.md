# Think About It

Answer these questions before checking `solutions/think-about-it-answers.md`.

## Predict the output

1. What is displayed after running the following lines?

   ```python
   print("Data", "Analytics", sep="-")
   print("Ready", end="!")
   print("Go")
   ```

2. What is displayed after running this block?

   ```python
   hours = 3
   minutes = 25
   total_minutes = hours * 60 + minutes
   print(total_minutes)
   ```

3. What is displayed after running the lines below?

   ```python
   amount = 8.5
   print("$" + format(amount, ".2f"))
   ```

## Multiple choice

4. What is the data type returned by `input()`?

   - A. `int`
   - B. `float`
   - C. `str`
   - D. It depends on what the user types.

5. Which statement converts the text `"12"` to an integer?

   - A. `number = str("12")`
   - B. `number = int("12")`
   - C. `number = float(int)`
   - D. `number = input(12)`

6. Which is the best named constant for the number of months in a year?

   - A. `monthsInYear`
   - B. `12`
   - C. `MONTHS_PER_YEAR`
   - D. `input_months`

7. Which expression calculates 15% of `price`?

   - A. `price + 0.15`
   - B. `price * 0.15`
   - C. `price / 15`
   - D. `15 * price + 100`

## Find and fix the problem

8. This code should add two whole numbers entered by the user. What must change?

   ```python
   first = input("First number: ")
   second = input("Second number: ")
   total = first + second
   print(total)
   ```

9. What is the problem with this code?

   ```python
   2nd_score = 87
   print(2nd_score)
   ```

10. Correct the `print()` statement so the price displays with two decimal places.

    ```python
    price = 4.5
    print("Price: $" + price)
    ```
