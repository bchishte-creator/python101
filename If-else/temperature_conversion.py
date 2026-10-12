unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ")
temp = float(input("Enter the temperature: " ))

if unit == "C":
    temp = round((temp * 9/5) + 32, 1)
    unit = "F"
    print(f"The temperature is: {temp} {unit}")
elif unit == "F":
    temp = round((temp - 32) * 5/9, 1)
    unit = "C"
    print(f"The temperature is: {temp} {unit}")
else:
    print(f"{unit} was not valid unit of temperature. Please enter C for Celsius or F for Fahrenheit.")
