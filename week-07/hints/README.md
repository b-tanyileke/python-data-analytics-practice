# Week 7 Hints

Use one hint at a time. Try the question again after each hint before reading
the solution.

## Question 13: Create a NumPy array

Pass the list to `np.array()`. Use the `dtype` argument to request floating-
point values.

## Question 14: Slice a 2D array

Use row and column slices separated by a comma. The ending index of a slice is
not included.

## Question 15: Boolean indexing

Call `copy()` first. The expression `updated_values < 0` produces a Boolean
array that can be used inside square brackets.

## Question 16: Row totals

Use the array `sum()` method. `axis=1` calculates one total for each row.

## Question 17: Transpose and scale

Use `.T` to transpose the array. Multiplying a NumPy array by one number
multiplies every element.

## Question 18: Pseudorandom matrix

Call `np.random.seed(seed)` before generating values. Use
`np.random.randint(0, 2, size=(2, 3))` to produce zeros and ones.
