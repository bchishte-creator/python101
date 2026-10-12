# Format specifiers = {Value:flags} format a value based on what flags are inserted

price1 = 49.5234
price2 = -45.435
price3 = 50.45245
price4 = 60.4325

# print(f"Price 1: ${price1:.2f}") #it means that the value will be formatted to 2 decimal places
# print(f"Price 2: ${price2:.2f}")
# print(f"Price 3: ${price3:.2f}")
# print(f"Price 4: ${price4:.2f}")


print(f"Price 1: ${price1:10}") #this means that the value will be formatted to 10 spaces 
print(f"Price 2: ${price2:10}")
print(f"Price 3: ${price3:10}")
print(f"Price 4: ${price4:10}")
