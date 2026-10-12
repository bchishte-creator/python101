# Typecasting converts a value from one data type to another.
# Common conversion functions are int(), float(), str(), and bool().

# Start with values of different types.
name = "Baha"       # str: text
age = 25             # int: whole number
gpa = 3.8            # float: decimal number
is_student = True    # bool: True or False

# Use type() to check a value's current data type.
print("Starting type of age:", type(age))
print("Starting type of gpa:", type(gpa))
print("Starting type of is_student:", type(is_student))

# Convert the integer age to a string.
age = str(age)
print("Age as text:", age)

# Both values are strings, so + joins them instead of adding numerically.
# The result is "251", not 26.
age += "1"
print("Text after joining '1':", age)

# Convert the float to an integer. int() discards the decimal part; it does
# not round, so 3.8 becomes 3.
gpa = int(gpa)
print("GPA as an integer:", gpa)

# Convert the Boolean True to the string "True".
# print() does not show quote marks around strings, so check its type too.
is_student = str(is_student)
print("Student value as text:", is_student)
print("Type after converting to text:", type(is_student))

# A non-empty string converts to True. An empty string converts to False.
# This does not check whether the text literally says "True" or "False".
name_is_nonempty = bool(name)
print("Is the name non-empty?:", name_is_nonempty)