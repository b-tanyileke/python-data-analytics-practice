"""Exercise 2 sample solution."""


def copy_and_add(items, new_item):
    """Return a copy of items with new_item added when it is not present."""
    updated_items = items.copy()

    if new_item not in updated_items:
        updated_items.append(new_item)

    return updated_items
