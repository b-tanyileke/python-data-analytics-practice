# Think About It

Answer the questions before checking `solutions/think-about-it-answers.md`.

## Predict the output

1. What is displayed?

   ```python
   temperature = 18

   if temperature >= 20:
       print("Warm")
   else:
       print("Cool")
   ```

2. What is displayed?

   ```python
   def double(number):
       return number * 2

   result = double(4)
   print(result)
   ```

3. What is displayed?

   ```python
   def message(name):
       greeting = "Hello, " + name
       return greeting

   print(message("Amina"))
   ```

## Multiple choice

4. Which operator tests whether `score` is equal to 10?

   - A. `score = 10`
   - B. `score == 10`
   - C. `score != 10`
   - D. `score >= 10`

5. Which value is a Boolean value in Python?

   - A. `"True"`
   - B. `true`
   - C. `True`
   - D. `YES`

6. Which condition is true only when `age` is at least 18 and `has_id` is `True`?

   - A. `age >= 18 or has_id`
   - B. `age >= 18 and has_id`
   - C. `age == 18 and has_id == "True"`
   - D. `age > 18 or has_id == True`

7. What does a value-returning function use to send a result back to its caller?

   - A. `print`
   - B. `input`
   - C. `return`
   - D. `import`

8. Which statement imports the standard `math` module?

   - A. `include math`
   - B. `load math`
   - C. `import math`
   - D. `math import`

9. Where can a local variable be used?

   - A. Anywhere in the program
   - B. Only inside the function where it is created
   - C. Only after `main()` is called
   - D. Only in another module

## Find and fix the problem

10. This code should display `Pass` when `score` is 60 or higher. Correct the condition.

    ```python
    score = 75
    if score = 60:
        print("Pass")
    ```

11. This function should return the sum of its two arguments. Correct it.

    ```python
    def add_numbers(first, second):
        print(first + second)
    ```

12. This code should handle division by zero without stopping the program. Correct the `except` line.

    ```python
    try:
        result = 10 / 0
    except ZeroDivisionError
        print("Cannot divide by zero.")
    ```
