
# PYTHON INPUT: EXAM REVIEW
# =========================

# input() displays a prompt, waits for the user to type something,
# and always returns the entered value as a string (str).


# 1. READ TEXT INPUT
# ------------------

# The user's name is text, so it can be stored directly as a string.

name = input("What is your name?: ")


# 2. READ A NUMBER AND CONVERT IT
# ------------------------------

# input() always returns a string.
# int() converts the entered text into a whole number (integer).

# Here, the user's age is converted to an integer,
# then 1 is added before the result is stored in age.

age = int(input("What is your age?: ")) + 1

# This is equivalent to writing:

age = int(input("What is your age?: "))
age += 1

# age += 1 means:
#
# age = age + 1


# IMPORTANT:
# If the user enters something that cannot be converted into an integer,
# Python will raise a ValueError.

# Example:
#
# int("20")       -> works
# int("twenty")   -> ValueError
# int("20.5")     -> ValueError


# 3. DISPLAY VALUES WITH AN F-STRING
# ----------------------------------

# Put f before the opening quotation mark.
# Then place variables or expressions inside {curly braces}.

print(f"Hello, {name}! Next year you will be {age}.")


# EXERCISE 1: CALCULATE A RECTANGLE'S AREA
# -----------------------------------------

# Use float() when the number may contain decimal values,
# such as 2.5, 7.25, or 10.0.

length = float(input("Enter the length in cm: "))
width = float(input("Enter the width in cm: "))

# Rectangle area:
# area = length × width

area = length * width

# The f-string inserts the value of area into the output.

print(f"The area of the rectangle is: {area} cm^2")


# EXERCISE 2: SHOPPING CART TOTAL
# --------------------------------

# Ask the user what item they want to buy.

item = input("What item would you like to buy?: ")

# float() is used for price because prices can contain decimals.

price = float(input(f"What is the price of {item}?: $"))

# int() is used for quantity because we normally buy
# a whole number of items.

quantity = int(input(f"How many {item}s would you like to buy?: "))

# Calculate the total cost.

total = price * quantity

# :.2f displays the number with exactly 2 digits after the decimal point.
# This is useful when displaying currency.

print(
    f"You bought {quantity} {item}s for a total of ${total:.2f}. "
    f"Thank you for shopping with us!"
)


# UNDERSTANDING :.2f AND round()
# --------------------------------

# :.2f is formatting syntax used inside an f-string.
#
# It means:
#
# :    -> begin formatting instructions
# .2   -> show 2 digits after the decimal point
# f    -> format the value as a floating-point number


# Example:

money = 12.5

print(f"${money:.2f}")

# Output:
# $12.50


# Another example:

money = 12.5678

print(f"${money:.2f}")

# Output:
# $12.57


# IMPORTANT:
# :.2f controls how the number is DISPLAYED.
# It does NOT permanently change the value stored in the variable.


number = 12.5678

print(f"{number:.2f}")

# Output:
# 12.57

# But number itself is still:
# 12.5678


# IF YOU WANT TO ROUND THE NUMBER OUTSIDE AN F-STRING
# ---------------------------------------------------

# Use the round() function.

# Syntax:
#
# round(number, decimal_places)


number = 12.5678

rounded_number = round(number, 2)

print(rounded_number)

# Output:
# 12.57


# The 2 means:
# round the number to 2 decimal places.


# Another example:

price = 9.87654

price = round(price, 2)

print(price)

# Output:
# 9.88


# You can choose a different number of decimal places.

number = 12.56789

print(round(number, 1))   # 12.6
print(round(number, 2))   # 12.57
print(round(number, 3))   # 12.568


# DIFFERENCE BETWEEN :.2f AND round()
# -----------------------------------

# :.2f
# -> used mainly when DISPLAYING a number
# -> used inside an f-string
# -> gives exactly 2 digits after the decimal point


number = 5

print(f"{number:.2f}")

# Output:
# 5.00


# round(number, 2)
# -> used when you want a rounded NUMBER
# -> can be stored in a variable
# -> can be used in later calculations


number = 12.5678

rounded_number = round(number, 2)

print(rounded_number)

# Output:
# 12.57


# IMPORTANT DIFFERENCE:
#
# :.2f is DISPLAY formatting.
# round() changes the numeric result you are working with.


# Example:

total = 10.56789

# Display only:
print(f"${total:.2f}")

# total is still 10.56789


# Store a rounded value:

total = round(total, 2)

# Now total contains the rounded result:
# 10.57


# ONE SMALL DETAIL TO REMEMBER
# -----------------------------

# round() does not guarantee that trailing zeros will be displayed.

number = round(5.0, 2)

print(number)

# Output may be:
# 5.0

# NOT:
# 5.00


# If you specifically want exactly 2 decimal places to appear,
# use :.2f when displaying it.

print(f"{number:.2f}")

# Output:
# 5.00


# SHOPPING CART EXAMPLE USING BOTH
# ---------------------------------

price = 4.567
quantity = 3

total = price * quantity

# Round total if you want to store a rounded numeric value.

rounded_total = round(total, 2)

# Then use :.2f when displaying currency.

print(f"Total: ${rounded_total:.2f}")


# CORRECT:

total = price * quantity
print(f"${total:.2f}")


# ALSO CORRECT:

total = price * quantity
total = round(total, 2)

print(total)


# INCORRECT:

# total = .2f

# total = price * quantity:.2f

# :.2f belongs inside the { } of an f-string.

# EXERCISE 3: MADLIBS GAME
# word game where you create a story by filling in the blanks with words provided by the user.
# --------------------------------

adjective = input("Enter and adjective (description): ")
noun1 = input("Enter a noun (person, place, or thing): ")
adjective2 = input("Enter another adjective (description): ") 
verb1 = input("Enter a verb with ing (action): ")
adjective3 = input("Enter another adjective (description): ")

print(f"Today I went to a {adjective} zoo.")
print(f"In an exhibit, I saw a {noun1}")
print(f"{noun1} was {adjective2} and {verb1}.")
print(f"I was {adjective3}!")


# QUICK REVIEW
# ============

# - input(prompt) displays a prompt and always returns a string.

# - str means string/text.

# - int(value) converts valid whole-number text into an integer.

# - float(value) converts valid numeric text into a floating-point number.

# - Use int() when you need whole numbers.

# - Use float() when decimal values may be needed.

# - Convert input before doing numerical arithmetic.

# - f-strings allow variables and expressions to be placed inside
#   strings using {curly braces}.

# - Example:
#
#   name = "Baha"
#   print(f"Hello, {name}!")

# - :.2f displays a number with exactly 2 decimal places.

# - Example:
#
#   price = 5
#   print(f"${price:.2f}")
#
#   Output:
#   $5.00


# - round(number, 2) rounds a numeric value to 2 decimal places.

# - Example:
#
#   number = 12.5678
#   number = round(number, 2)
#
#   number is now approximately:
#   12.57


# EXAM MEMORY TRICK
# =================

# input()              -> gives you STRING
# int(input())         -> gives you INTEGER
# float(input())       -> gives you FLOAT

# f"{variable}"        -> puts a value inside displayed text

# f"{number:.2f}"      -> DISPLAY with exactly 2 decimal places

# round(number, 2)     -> ROUND a number to 2 decimal places