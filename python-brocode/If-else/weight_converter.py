# # python weight converter

# weight = float(input("Enter the weight: "))
# unit = input("Enter the unit (K for kilograms, L for pounds): ")

# if unit == "K":
#     weight = weight * 2.205
#     unit = "Lbs"

# elif unit == "L":
#     weight = weight / 2.205
#     unit = "Kgs"
# else:
#     print(f"{unit} was not valid")

# print(f"Your weight is: {weight} {unit}")



#----Python Weight Converter -----

weight = float(input("Enter the weight: "))
unit = input("Enter the unit (K for kilograms, L for pounds): ")


if unit == "K":
    weight = weight * 2.205
    unit = "Lbs"

elif unit == "L":
    weight = weight / 2.205
    unit = "Kgs"
else:
    print(f"{unit} was not valid")

print(f"Your weight is: {weight} {unit}")