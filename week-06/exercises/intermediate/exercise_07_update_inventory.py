"""Exercise 7: Update inventory

Write a function called update_inventory that accepts two dictionaries:

- inventory maps item names to the quantities currently available.
- sales maps item names to the quantities sold.

Make a copy of inventory. For each item in sales, subtract the quantity sold
from that item's quantity in the copy. Return the updated copy. Every sales
item is guaranteed to be in inventory, and no sale quantity is larger than the
available quantity.

Do not change the original inventory dictionary.

For example:
- update_inventory({"pens": 20, "notebooks": 12},
  {"pens": 3, "notebooks": 5}) should return
  {"pens": 17, "notebooks": 7}.
"""


# Write your function below.
