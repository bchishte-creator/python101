# While loop = excute some code as long as a condition is true

# name = input("Enter your name: ")

# while name == "":
#     print("You didn't enter your name!")
#     name = input("Enter your name: ")

# print(f"Hello {name}!")
# ------


# food = input("What is your favorite food? ")

# while not food == "":
#     print(f"You like {food}!")
#     food = input("What is your favorite food? ")

# print("Bye")

age = int(input("How old are you? "))

while age <= 0 or age > 100:
    print("You can't be negative or over 100 years old!")
    age = int(input("How old are you? "))
print(f"You are {age} years old!")
