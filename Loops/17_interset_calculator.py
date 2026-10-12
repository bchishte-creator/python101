
## Example 5

# principle = 0 
# rate = 0
# time = 0

# while principle <= 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle <= 0:
#         print("Principle amount must be greater than 0!")

# while rate <= 0:
#     rate = float(input("Enter the rate of interest: "))
#     if rate <= 0:
#         print("Rate of interest must be greater than 0!")

# while time <= 0:
#     time = float(input("Enter the time in years: "))
#     if time <= 0:
#         print("Time must be greater than 0!")

# total = principle * pow((1 + (rate / 100)), time)
# print (f"The total amount after {time} years is: {total:.2f}")


# principle = 0 
# rate = 0
# time = 0

# while principle < 0:
#     principle = float(input("Enter the principle amount: "))
#     if principle < 0:
#         print("Principle amount must be greater than 0!")

# while rate < 0:
#     rate = float(input("Enter the rate of interest: "))
#     if rate < 0:
#         print("Rate of interest must be greater than 0!")

# while time < 0:
#     time = float(input("Enter the time in years: "))
#     if time < 0:
#         print("Time must be greater than 0!")

# total = principle * pow((1 + (rate / 100)), time)
# print (f"The total amount after {time} years is: {total:.2f}")


#this will not work and go stay to the result becuase the while loop will not be executed because the condition is not met. The condition is that the principle, rate, and time must be greater than 0. If the user enters a negative value for any of these variables, the while loop will not be executed and the program will go to the result.

# to avoid this we can use while true and break statement to exit the loop when the condition is met. This way, the while loop will always be executed and the user will be prompted to enter a valid value for principle, rate, and time until they enter a valid value.

#here is how we can do it:


principle = 0 
rate = 0
time = 0

while True:
    principle = float(input("Enter the principle amount: "))
    if principle < 0:
        print("Principle amount must be greater than 0!")
    else:
        break

while True:
    rate = float(input("Enter the rate of interest: "))
    if rate < 0:
        print("Rate of interest must be greater than 0!")
    else:
        break

while True:
    time = float(input("Enter the time in years: "))
    if time < 0:
        print("Time must be greater than 0!")
    else:
        break

total = principle * pow((1 + (rate / 100)), time)
print (f"The total amount after {time} years is: {total:.2f}")


#now you have to understand the difference between the two while loops. The first while loop will not be executed if the user enters a negative value for principle, rate, or time. The second while loop will always be executed until the user enters a valid value for principle, rate, and time. This is because the second while loop uses a break statement to exit the loop when the condition is met.
