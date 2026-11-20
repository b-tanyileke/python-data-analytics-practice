# Part A: Multiple-Choice Questions

Choose one alternative that best completes the statement or answers the
question. Check your answers only after attempting every question.

1. Which statement best describes a NumPy `ndarray`?

   - A. A dictionary that stores only numerical keys
   - B. A fixed-size, homogeneous N-dimensional array
   - C. A Python list that can store any data type
   - D. A file object used to read numerical data

2. What is the data type of every element in this array?

   ```python
   import numpy as np

   values = np.array([1, 2, 3.5])
   ```

   - A. `int`
   - B. `float`
   - C. `str`
   - D. The array has mixed element types

3. What is displayed?

   ```python
   import numpy as np

   numbers = np.arange(6).reshape(2, 3)
   print(numbers.shape)
   ```

   - A. `(6,)`
   - B. `(2, 3)`
   - C. `(3, 2)`
   - D. `6`

4. What is displayed?

   ```python
   import numpy as np

   values = np.array([2, 4, 6])
   print(values * 3)
   ```

   - A. `[6, 12, 18]`
   - B. `[2, 4, 6, 2, 4, 6, 2, 4, 6]`
   - C. `36`
   - D. An error

5. What is displayed?

   ```python
   import numpy as np

   values = np.array([10, 20, 30, 40, 50])
   print(values[1:4])
   ```

   - A. `[10 20 30]`
   - B. `[20 30 40]`
   - C. `[20 30 40 50]`
   - D. `[10 20 30 40]`

6. Given the following array, which expression returns `5`?

   ```python
   import numpy as np

   matrix = np.array([[1, 2, 3], [4, 5, 6]])
   ```

   - A. `matrix[1, 1]`
   - B. `matrix[0, 1]`
   - C. `matrix[1, 0]`
   - D. `matrix[2, 2]`

7. What is displayed?

   ```python
   import numpy as np

   values = np.array([3, 8, 2, 9])
   print(values[values > 5])
   ```

   - A. `[ True  True False  True]`
   - B. `[3 8 2 9]`
   - C. `[8 9]`
   - D. `[3 2]`

8. What is displayed?

   ```python
   import numpy as np

   matrix = np.array([[1, 2, 3], [4, 5, 6]])
   print(matrix.T)
   ```

   - A. `[[1 2 3] [4 5 6]]`
   - B. `[[6 5 4] [3 2 1]]`
   - C. `[[1 4] [2 5] [3 6]]`
   - D. An error because the matrix is not square

9. What does `np.where(condition, x, y)` do?

   - A. Selects values from `x` or `y` according to `condition`
   - B. Sorts `x` and `y` in ascending order
   - C. Removes all values that do not satisfy `condition`
   - D. Finds the index of the largest value in `x`

10. Which expression creates an array containing the integers 0 through 9?

    - A. `np.array(10)`
    - B. `np.arange(10)`
    - C. `np.zeros(10, 1)`
    - D. `np.reshape(10)`

11. What is displayed?

    ```python
    import numpy as np

    values = np.array([-2, 0, 5])
    print(values >= 0)
    ```

    - A. `[-2 0 5]`
    - B. `[False  True  True]`
    - C. `[ True False False]`
    - D. `[0 1 1]`

12. Which function can generate an array of pseudorandom integers?

    - A. `np.random.randint()`
    - B. `np.array.randint()`
    - C. `np.arange.random()`
    - D. `np.reshape.randint()`
