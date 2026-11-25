# Part A: Multiple Choice

Choose one best answer. Assume `import pandas as pd`.

1. Which expression removes rows containing at least one missing value?

   - A. `df.dropna()`
   - B. `df.fillna()`
   - C. `df.isna()`
   - D. `df.replace()`

2. What does `df.fillna(0)` return by default?

   - A. A new DataFrame with missing values replaced by 0
   - B. The number of missing values
   - C. A DataFrame with zero-valued rows removed
   - D. The original DataFrame modified in place

3. Given `df.drop_duplicates()`, which rows are removed by default?

   - A. Every row that contains any missing value
   - B. Later rows identical across all columns
   - C. Every row with a duplicate index label
   - D. The first occurrence of every duplicate row

4. What does `s.map({"NY": "New York", "TX": "Texas"})` return for
   a value `"CA"` that is not a key in the dictionary?

   - A. `"CA"`
   - B. `0`
   - C. A missing value
   - D. An error in every case

5. Which expression returns a DataFrame with column `old` renamed to `new`?

   - A. `df.rename(columns={"old": "new"})`
   - B. `df.rename(index={"old": "new"})`
   - C. `df.replace(columns={"old": "new"})`
   - D. `df.rename("old", "new")`

6. With `pd.cut(s, bins=[0, 10, 20])` and default settings, which interval
   contains the value 10?

   - A. `(0, 10]`
   - B. `(10, 20]`
   - C. Both intervals
   - D. Neither interval

7. Why specify `random_state` when sampling rows with `df.sample()`?

   - A. To make the sample reproducible for the same data and settings
   - B. To remove missing values
   - C. To guarantee ascending order
   - D. To change the number of columns

8. What does `pd.get_dummies()` generally create from a categorical column?

   - A. An indicator column for each category
   - B. One row for each missing value
   - C. A sorted list of column names
   - D. A single numerical average
