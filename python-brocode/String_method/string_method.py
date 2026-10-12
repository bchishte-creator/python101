# from unittest import result

# # name  = input("Enter your full name: ")
# phone_number = input("Enter your phone number: ")
# # result = len(name)
# # result = name.find("B")
# # result = name.rfind("a")

# result  = phone_number.count("-")

# result2 = phone_number = phone_number.replace("-", "")

# print(result2)

# -----
# print (help(str)) # help function to get all the methods of a string


# --- Exercises ----

#Validate user input exercise

# Q1.username is no more than 12 characters
# Q2. username must not contain any spaces
# Q3. username must contain digits

# ----------Ans to the Questions -------------
username = input("Enter your username: ")


if len(username) > 12: 
    print("Username must be no more than 12 characters")

elif not username.find(" ") == -1: 
    print(" Your username can't contain spaces")

    # you may notice we use not after elif because we want to check if the username contains spaces. If it does, then we print the message. If it doesn't, then we print the welcome message. We use not because we want to check if the username does not contain spaces. We use find() method to check if the username contains spaces. If it does, then find() method returns the index of the first occurrence of the space character. If it doesn't, then find() method returns -1. So, we use not to check if the username does not contain spaces.

elif not username.isalpha():
    print(" Your username can not contain digital or special characters")

    #note: we use isalpha() method to check if the username contains only alphabetic characters. We use not to check if the username does not contain only alphabetic characters.

else: 
    print(f"Welcome {username}!")
