"""Exercise 7: Mailbox line analysis

Write a function called count_sender_lines that accepts a filename. The file
contains text lines from a mailbox. Read the file one line at a time and count
only the lines that begin with `From ` (the word From followed by one space).
Do not count lines that begin with `From:`.

Return the number of sender lines.

For example, if a file contains:

```text
From alex@example.com Tue Sep 1
From: alex@example.com
Hello class
From sam@example.com Wed Sep 2
```

then count_sender_lines(filename) should return 2.
"""


# Write your function below.
