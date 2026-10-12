"""A practical guide to Python's (), [], and {} delimiters."""

import math


# MEMORY RULE
# () do something: call a function, group an expression, or make a tuple.
# [] get something: access an item or a slice.
# {} name/map things: make a dictionary or set, or mark a value in an f-string.


print("1. Parentheses: ()")

# Call a function: the value goes inside the function's parentheses.
number = 25
root = math.sqrt(number)
print("Square root:", root)

# Group calculations when you want to make the order clear.
calculation = (2 + 3) * 4
print("Grouped calculation:", calculation)

# Parentheses can also create a tuple. A one-item tuple needs a comma.
point = (3, 7)
one_item_tuple = ("Python",)
print("Point:", point)
print("One-item tuple:", one_item_tuple)


print("\n2. Square brackets: []")

# Get an item by its position. Positions start at 0; -1 means the last item.
colors = ["red", "green", "blue"]
print("First color:", colors[0])
print("Last color:", colors[-1])

# A slice is [start:stop]; stop is not included.
print("First two colors:", colors[0:2])
print("Every other number:", [10, 20, 30, 40][::2])


print("\n3. Curly braces: {}")

# A dictionary maps keys to values. Use a key to get its value.
student = {"name": "Amina", "score": 92}
print("Student name:", student["name"])

# A set stores unique values. An empty set is set(), not {}.
unique_numbers = {2, 2, 5}
empty_set = set()
empty_dictionary = {}
print("Unique numbers:", unique_numbers)
print("Empty set:", empty_set)
print("Empty dictionary:", empty_dictionary)


print("\n4. F-strings: {} put values into text")

# In an f-string, braces hold a variable or expression.
name = "Amina"
print(f"Hello, {name}!")

# The colon starts a format specifier. .2f means 2 digits after the decimal.
print(f"Pi to 2 decimal places: {math.pi:.2f}")

# , adds thousands separators; >8.2f right-aligns in a width of 8 characters.
price = 1234.5
print(f"Price: {price:>10,.2f}")


print("\n5. Put the pieces together")

measurements = [9, 16]
# Read two list items, add them, call sqrt(), then format the result in the f-string.
result = math.sqrt(measurements[0] + measurements[1])
print(f"Square root of {measurements[0]} + {measurements[1]} = {result:.2f}")

# Read the combined expression from the inside out:
# measurements[0] -> add the values -> math.sqrt(...) -> {result:.2f} -> print(...)