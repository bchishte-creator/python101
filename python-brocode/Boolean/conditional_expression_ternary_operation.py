# Conditional expressions = A one line shortcut for if-else statements. Also called ternary operations. It print or assign one of two values based on a condition. X if condition else Y

num = 7
a = 6
b = 8
age = 17
temperature = 25
user_role = "admin"

# print("positive" if num > 0 else "negative")
# print ("negative" if num < 0 else "positive" if num > 0 else "zero")
# max_num = a if a > b else b
# min_num = a if a < b else b
# status = "Adult" if age >= 18 else "Minor"
# weather = "Hot" if temperature > 30 else "Warm" if temperature > 20 else "Cold"

access_level = "Full Access" if user_role == "admin" else "Limited access"

print(access_level)