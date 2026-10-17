# Think About It

Answer the questions before checking `solutions/think-about-it-answers.md`.

## Predict the output

1. What is displayed?

   ```python
   colors = ["blue", "green", "red"]
   print(colors[1])
   ```

2. What is displayed?

   ```python
   numbers = [2, 4, 6]
   numbers.append(8)
   print(len(numbers))
   ```

3. What is displayed?

   ```python
   settings = {"theme": "dark", "font_size": 14}
   settings["font_size"] = 16
   print(settings["font_size"])
   ```

4. What is displayed?

   ```python
   point = (5, 2)
   x_coordinate, y_coordinate = point
   print(x_coordinate + y_coordinate)
   ```

5. What is displayed?

   ```python
   values = [3, 3, 5, 7, 7]
   unique_values = set(values)
   print(len(unique_values))
   ```

## Multiple choice

6. Which expression makes a copy of the list `names`?

   - A. `names.copy()`
   - B. `names.append()`
   - C. `names.keys()`
   - D. `names.strip()`

7. Which dictionary expression returns the value stored for the key `"score"`?

   - A. `scores("score")`
   - B. `scores["score"]`
   - C. `scores.add("score")`
   - D. `scores.copy("score")`

8. Which collection stores values without duplicates?

   - A. A list
   - B. A dictionary
   - C. A set
   - D. A string

9. Which statement correctly creates a tuple containing `"Amina"` and `92`?

   - A. `["Amina", 92]`
   - B. `{"Amina": 92}`
   - C. `("Amina", 92)`
   - D. `"Amina", "92"`

10. Given `matrix = [[1, 2], [3, 4]]`, which expression returns `4`?

    - A. `matrix[1][1]`
    - B. `matrix[0][1]`
    - C. `matrix[1]`
    - D. `matrix[2][2]`

## Find and fix the problem

11. This code should add `"folder"` to the end of the list. Correct the list
    method.

    ```python
    supplies = ["pen", "paper"]
    supplies.add("folder")
    ```

12. This code should display the value for the key `"city"`. Correct the
    dictionary access.

    ```python
    address = {"city": "Chicago"}
    print(address.city)
    ```

13. This code should display both values in the tuple. Correct the assignment.

    ```python
    point = (3, 4)
    x_coordinate = y_coordinate = point
    print(x_coordinate, y_coordinate)
    ```
