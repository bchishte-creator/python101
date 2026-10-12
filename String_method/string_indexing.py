# indexing = accessing elements of a sequence using [] (indexing operator). Indexing starts from 0. The first element of a sequence has index 0, the second element has index 1, and so on. The last element of a sequence has index -1, the second last element has index -2, and so on.

# [start : end : step] = slicing operator. The start index is inclusive, the end index is exclusive, and the step index is optional. The default value of start index is 0, the default value of end index is the length of the sequence, and the default value of step index is 1.

credit_number = "1234 5678 9012 3456"


# print(credit_number[0:4]) # prints the first 4 digits of the credit card number it exclude the 4th index which is the space character

# print(credit_number[:4]) # prints the first 4 digits of the credit card number. It exclude the 4th index which is the space character. if we don't specify the start index, it will default to 0.

# print(credit_number[5:9]) # prints the second 4 digits of the credit card number. It exclude the 9th index which is the space character. Its also called slicing. Slicing is used to get a subsequence of a sequence. Slicing is done using the slicing operator [] with the start index, end index, and step index. The start index is inclusive, the end index is exclusive, and the step index is optional. The default value of start index is 0, the default value of end index is the length of the sequence, and the default value of step index is 1.

# print(credit_number[5:]) # prints the second 4 digits of the credit card number. It exclude the 9th index which is the space character. if we don't specify the end indprint(credit_number[-1]) # prints the last digit of the credit card number It does not include the last index which is the space character. Here it did not start from 0 because we used negative indexing. The last index is -1, the second last index is -2, and so on. This is not slicing, this is indexing. Indexing is used to access elements of a sequence using [] (indexing operator). Indexing starts from 0. The first element of a sequence has index 0, the second element has index 1, and so on. The last element of a sequence has index -1, the second last element has index -2, and so on.
# ex, it will default to the length of the sequence. Its also called slicing. Slicing is used to get a subsequence of a sequence. Slicing is done using the slicing operator [] with the start index, end index, and step index. The start index is inclusive, the end index is exclusive, and the step index is optional. The default value of start index is 0, the default value of end index is the length of the sequence, and the default value of step index is 1.

# print(credit_number[-1]) # prints the last digit of the credit card number It does not include the last index which is the space character. Here it did not start from 0 because we used negative indexing. The last index is -1, the second last index is -2, and so on. This is not slicing, this is indexing. Indexing is used to access elements of a sequence using [] (indexing operator). Indexing starts from 0. The first element of a sequence has index 0, the second element has index 1, and so on. The last element of a sequence has index -1, the second last element has index -2, and so on.

# print(credit_number[-4]) # prints the last 4 digits of the credit card number. It does not include the last index which is the space character. Here it did not start from 0 because we used negative indexing. The last index is -1, the second last index is -2, and so on. This is also not slicing since we only used one index. Indexing is used to access elements of a sequence using [] (indexing operator). Indexing starts from 0. The first element of a sequence has index 0, the second element has index 1, and so on. The last element of a sequence has index -1, the second last element has index -2, and so on. On the other hand, slicing is used to get a subsequence of a sequence. Slicing is done using the slicing operator print(credit_number[-1]) # prints the last digit of the credit card number It does not include the last index which is the space character. Here it did not start from 0 because we used negative indexing. The last index is -1, the second last index is -2, and so on. This is not slicing, this is indexing. Indexing is used to access elements of a sequence using [] (indexing operator). Indexing starts from 0. The first element of a sequence has index 0, the second element has index 1, and so on. The last element of a sequence has index -1, the second last element has index -2, and so on.
# [] with the start index, end index, and step index. The start index is inclusive, the end index is exclusive, and the step index is optional. The default value of start index is 0, the default value of end index is the length of the sequence, and the default value of step index is 1. But if it's minus indexing, the default value of start index is -1, the default value of end index is the negative length of the sequence, and the default value of step index is -1.

# print(credit_number[-4:]) # prints the last 4 digits of the credit card number. It does not include the last index which is the space character. Slicing operator is used here. The start index is -4, the end index is not specified, so it will default to the length of the sequence. How it slicing works is that it starts from the start index and goes up to the end index, but it does not include the end index. So, in this case, it starts from -4 and goes up to the length of the sequence, but it does not include the length of the sequence.

# # Slicing and some similar methods like split() and join() are used to manipulate strings. For example, we can use slicing to get the first 4 digits of the credit card number and then use join() to join them together with a space character. Slicing is connected with python indexing. Indexing is used to access elements of a sequence, and slicing is used to get a subsequence of a sequence. Slicing is done using the slicing operator [] with the start index, end index, and step index. The start index is inclusive, the end index is exclusive, and the step index is optional. The default value of start index is 0, the default value of end index is the length of the sequence, and the default value of step index is 1.


# #---------Step Field -------  

# # using step field we can access the characters in a string by a give step. We can count by twos or we can count by threes.

# print(credit_number[::2]) #This will print every second character of the string.


# print(credit_number[::3]) #This will print every third character of the string.

# #--- Here's a program of getting the last 4 digit ---

# last_digit= credit_number[-4:]
# print(f"xxxx-xxxx-xxxx-{last_digit}")


# # -----Reverse the character in the string ------
# print(credit_number[::-1]) #this is called step slicing. It starts from the end of the string and goes to the beginning of the string. The start index is not specified, so it will default to the length of the sequence. The end index is not specified, so it will default to the length of the sequence. The step index is -1, which means it will go backwards. So, in this case, it starts from the end of the string and goes to the beginning of the string. what if you write something like this: 




# print(credit_number[2:4:-1]) # this will print an empty string because the start index is greater than the end index and the step index is -1. The start index is 2, the end index is 4, and the step index is -1. So, it starts from the end of the string and goes to the beginning of the string, but it does not include the end index. So, in this case, it starts from the end of the string and goes to the beginning of the string, but it does not include the end index. So, it will print an empty string. Here is how you can fix it: 

# print(credit_number[4:2:-1]) # this will print " 5" because the start index is greater than the end index and the step index is -1. The start index is 4, the end index is 2, and the step index is -1. So, it starts from the end of the string and goes to the beginning of the string, but it does not include the end index. So, in this case, it starts from the end of the string and goes to the beginning of the string, but it does not include the end index. So, it will print " 5".

# # #-- Real Example of a slicing and indexing use case ----

# # credit_card_number = input("Enter your credit card number: ")
# # last_digit = credit_card_number[-4:]    # indexing to get the last digit of the credit card number

# # print(f"Your credit card number is: {credit_card_number[:4]} **** **** {last_digit}") # slicing to get the first 4 digits of the credit card number and the last 4 digits of the credit card number. The middle 8 digits are replaced with asterisks for security reasons.

