""" Exercise 06 - Sample Solution """

SALES_TAX_RATE = 0.07
product_name = input("Product name: ")
unit_price = float(input("Unit price: "))
quantity = int(input("Quantity: "))
subtotal = unit_price * quantity
sales_tax = subtotal * SALES_TAX_RATE
total = subtotal + sales_tax
print("Receipt for: " + product_name)
print("Subtotal: $" + format(subtotal, ".2f"))
print("Sales tax: $" + format(sales_tax, ".2f"))
print("Total cost: $" + format(total, ".2f"))
