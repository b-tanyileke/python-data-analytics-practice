notebook_count = int(input("Number of notebooks: "))
notebook_price = float(input("Price of one notebook: "))
total_cost = notebook_count * notebook_price
print("Total cost: $" + format(total_cost, ".2f"))
