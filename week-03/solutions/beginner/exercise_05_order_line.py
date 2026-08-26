""" Exercise 05 - Sample Solution """

item_name = input("Item name: ")
quantity = int(input("Quantity: "))
unit_price = float(input("Unit price: "))
line_total = quantity * unit_price
print("Item: " + item_name, "Quantity: " + str(quantity), "Total: $" + format(line_total, ".2f"), sep=" | ")
