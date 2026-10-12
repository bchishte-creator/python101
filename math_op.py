

#friends = 10

# friends  = friends + 1
#or friends += 1
#friends = friends - 1
#or friends -= 1
#friends = friends * 2
# or friends *= 2
#friends = friends / 2
# or friends /= 2
#friends = friends **2 
#or friends **=2
#reminder = friends % 3
#or reminder = friends %= 3

#print(reminder)

## SECOND PART -----

# x = 3.50
# y = 4
# y2 = -4
# z  = 5


#result = round(x)
#result = abs(y2)
#result = pow(y, z)
# result1 = max(x, y, y2, z)
# result2 = min(x, y, y2, z)
# print(result1)
# print(result2)


## THIRD PART -----



# import math # note that we can not name our python file as math.py because it will conflict with the built in math module like math.sqrt() and math.pi. Also, we can not name our python file as random.py because it will conflict with the built in random module like random.randint() and random.choice().

# x = 9
# print(math.pi)
# print (math.e) # for physics use case
# print(f"{math.sqrt(x): .3f}") 

# square root of x. we use second bracket to format the output to 3 decimal places. You have to know when to use first bracket when to use second bracket and when to use third bracket nd when to use mix of them. Here is a breakdown of the brackets:
# 1st bracket: used for function calls like math.sqrt(x). 
# 2nd bracket: used for formatting the output like f"{math.sqrt(x): .3f}" 
# 3rd bracket: used for indexing like list[0]


# FOURTH PART ----- Real Maths use case

import math

# First exercise: Calculate the circumference and area of a circle given its radius. The formulas are:

# radius  = float (input("Enter the radius of the circle: "))
# circumference = 2 * math.pi * radius
# area = math.pi * radius ** 2
# print(f"The circumference of the circle is: {round(circumference)}") #this will round the value to nearest integer
# print(f"The circumference of the circle is: {round(circumference, 2)}") #this will round the value to 2 decimal places
# print(f"the area of the circle is: {round(area, 2)}")

# Second exercise: Hypothenuse of a right triangle given the lengths of the other two sides. The formula is:


a = float(input("Enter the length of side a: "))
b = float(input("Enter the length of side b: "))

c = math.sqrt(pow(a, 2) + pow(b, 2))

#  print(f"The length of the hypothenuse is: round.{c})") // # Incorrect: round.{c} prints the text "round." followed by c; it does not round c.
# In an f-string, put the expression inside {}. Use {round(c)} to round c.

print(f"The length of the hypothenuse is: {round(c)}")