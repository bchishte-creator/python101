# if = Do some code only if some condition is True 
# Else do something else 

age = int(input("Enter your age: "))

if age >= 100:
    print("You are too too old to sign up")
elif age >= 18:
    print("You are signed up")
elif age <= 0: 
    print("You haven't been born  yet!")
else: 
    print("You must be 18 plus to signed up")
    