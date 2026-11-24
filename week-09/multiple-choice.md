# Part A: Multiple Choice

Choose one best answer for each question. Assume `import pandas as pd`.

1. Which statement creates a Series using dictionary keys as labels?

   - A. `pd.Series({"Ada": 80, "Ben": 90})`
   - B. `pd.Series["Ada", "Ben"]`
   - C. `pd.index({"Ada": 80})`
   - D. `pd.DataFrame.Series(80, 90)`

2. Given `s = pd.Series([10, 20], index=["a", "b"])`, what does
   `s.loc["b"]` return?

   - A. `10`
   - B. `20`
   - C. `"b"`
   - D. An error

3. What does `df.isna()` return?

   - A. A Boolean DataFrame indicating missing values
   - B. A DataFrame with all missing rows removed
   - C. The number of columns
   - D. A sorted DataFrame

4. Given `s = pd.Series([2, 4])`, what values result from `s * 3`?

   - A. `2, 4, 2, 4, 2, 4`
   - B. `6, 12`
   - C. `5, 7`
   - D. An error

5. What does `df.reindex(["b", "a", "c"])` do by default when `"c"`
   is absent from the index?

   - A. Reorders the rows and adds a missing-valued row for `"c"`
   - B. Removes column `"c"`
   - C. Raises an error
   - D. Fills the new row with zero

6. Which expression sorts a DataFrame by the values in `score`, highest first?

   - A. `df.sort_values("score", ascending=False)`
   - B. `df.sort_index("score")`
   - C. `df.rank("score", descending=True)`
   - D. `df.sort_values("score", ascending=True)`

7. Given duplicate row labels, what can `df.loc["a"]` return when `"a"`
   occurs more than once?

   - A. A DataFrame containing the matching rows
   - B. Only the first matching value, always
   - C. A Boolean, always
   - D. Only the last matching row, always

8. What does `df.drop(columns=["score"])` return by default?

   - A. A new DataFrame without the `score` column
   - B. The deleted column only
   - C. A DataFrame with all rows removed
   - D. The original DataFrame changed in place
