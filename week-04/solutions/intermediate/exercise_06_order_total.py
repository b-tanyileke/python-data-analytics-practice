"""Exercise 6 sample solution."""

MEMBER_DISCOUNT = 0.10


def order_total(unit_price, quantity, membership_response):
    """ returns the total price based on the unit price, quantity, and membership response """
    subtotal = unit_price * quantity

    if membership_response == "yes" and subtotal >= 100:
        return subtotal * (1 - MEMBER_DISCOUNT)
    return subtotal
