# Week 10 Hints

Try each question before opening its solution.

- Question 9: Chain `.str.strip()` and `.str.lower()`, then use `dropna`,
  `drop_duplicates`, and `fillna` in the order requested.
- Question 10: Use `replace` for hours, `map` for department codes, and
  `rename(columns=...)` for the labels.
- Question 11: With `right=False`, bins `[0, 60, 101]` include 0 and 100 in
  the required bands. Supply the labels to `cut`, then call `get_dummies`.
- Question 12: Filter complete rows before removing duplicate names; call
  `sample(n=sample_size, random_state=42)` last.
