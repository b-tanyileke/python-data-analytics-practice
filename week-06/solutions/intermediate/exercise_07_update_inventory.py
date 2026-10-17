"""Exercise 7 sample solution."""


def update_inventory(inventory, sales):
    """Return a copy of inventory after subtracting the recorded sales."""
    updated_inventory = inventory.copy()

    for item in sales:
        updated_inventory[item] -= sales[item]

    return updated_inventory
