# Week 7: NumPy

This week's practice follows the two-part format used in the sample final:
multiple-choice questions followed by short-answer coding questions. It is
still an optional practice resource, not a graded exam.

## Topics

- NumPy arrays and array data types
- creating, reshaping, indexing, and slicing arrays
- 2D and 3D array access
- elementwise arithmetic and relational operations
- Boolean indexing
- transposing arrays and swapping axes
- pseudorandom number generation

## Question format

### Part A: Multiple-choice questions

Complete Questions 1–12 in [multiple-choice.md](multiple-choice.md). Each
question has four alternatives. Choose the one best answer before checking
`solutions/multiple-choice-answers.md`.

### Part B: Short-answer coding questions

Complete Questions 13–18 in `exercises/short-answer/`. Each file states the
required function, input, and expected result. Write NumPy code that produces
the requested result.

Use [hints/README.md](hints/README.md) only when a small nudge is needed.
Solutions are visible in `solutions/`; try each question before opening its
matching solution.

## Check your work

After writing your functions, run the following command from the repository
root:

```text
python -m pytest week-07/check_your_work.py
```

These checks use the files in `exercises/` and report which functions are
working. A failure is feedback for debugging, not a grade.

The separate files in `tests/` verify the included sample solutions and are
used to maintain the repository.
