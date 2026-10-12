# Python Basics: Exam Review

## 1. Variables and Data Types

A variable is a name that refers to a value. Python determines a variable's type from the value assigned to it.

```python
name = "Baha"       # str: text
age = 25             # int: whole number
gpa = 3.8            # float: decimal number
is_student = True    # bool: True or False
```

Use `type()` to check a value's type:

```python
print(type(age))  # <class 'int'>
```

The file [variable.py](variable.py) is currently empty, so these examples summarize the variables used in the other lesson files.

## 2. Getting Input and Calculating

`input()` displays a prompt and returns what the user types as a string. Convert the input before doing arithmetic with it.

```python
length = float(input("Enter the length: "))
width = float(input("Enter the width: "))
area = length * width

print(f"The area of the rectangle is: {area} cm²")
```

Here, `float()` allows decimal measurements. The expression `length * width` calculates the rectangle's area. The `f` before the string lets `{area}` be replaced with the value stored in the variable.

Review the original example in [user_input.py](user_input.py).

## 3. Type Conversion (Typecasting)

Typecasting converts a value from one type to another. Common built-in conversion functions are:

| Function | Converts to | Example |
| --- | --- | --- |
| `int(value)` | integer | `int("25")` gives `25` |
| `float(value)` | decimal number | `float("3.8")` gives `3.8` |
| `str(value)` | string | `str(25)` gives `"25"` |
| `bool(value)` | Boolean | `bool(0)` gives `False` |

Examples:

```python
age = 25
age = str(age)       # age is now the string "25"
age += "1"           # joins text, so age is now "251"

gpa = 3.8
gpa = int(gpa)       # becomes 3; int() truncates the decimal, it does not round

is_student = True
is_student = str(is_student)  # becomes the string "True"
print(is_student)              # displays True (without quote marks)
print(type(is_student))        # displays <class 'str'>
```

`print()` does not show quote marks around strings. Use `type()` when you need to distinguish the string `"True"` from the Boolean `True`.

Review the original example in [typecasting.py](typecasting.py).

## 4. Important Boolean Conversion Rule

`bool()` does not mean “convert only the words `True` or `False`.” In Python, empty values are false-like and non-empty values are true-like:

```python
bool("")       # False: empty string
bool("Baha")   # True: non-empty string
bool(0)        # False
bool(25)       # True
```

Therefore, `name = bool(name)` with `name = "Baha"` produces `True`; it does not raise a `ValueError`. The comment in the current `typecasting.py` example that says otherwise is incorrect.

## 5. Quick Exam Checks

- What type does `input()` return? A `str`.
- Why does `"25" + "1"` produce `"251"`? Both operands are strings, so `+` concatenates them.
- How can you add those values numerically? Convert them first, for example `int("25") + int("1")`, which gives `26`.
- What is `int(3.8)`? `3`; the fractional part is discarded.
- Why does `print(str(True))` display `True`? Printing a string does not display its quote marks.
- What does `bool("False")` return? `True`, because the string is non-empty.