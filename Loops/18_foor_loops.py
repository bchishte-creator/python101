# for loops  = execute a block of code a fixed number of times. The for loop is used when you know how many times you want to execute a block of code. The for loop is used to iterate over a sequence (list, tuple, dictionary, set, or string). This is less like the for keyword in other programming languages, and works more like an iterator method as found in other object-orientated programming languages.

# for x in (range(1, 11, 2)):
    # print(x)

# credit_card = "1234-5678-9012-3456"

# for x in credit_card:
#     print(x)


#continue and break are statements that can be used in for loops. The continue statement is used to skip the current iteration of the loop and move on to the next iteration. The break statement is used to exit the loop completely. They an also be used in while loops. The continue statement is used to skip the current iteration of the loop and move on to the next iteration. The break statement is used to exit the loop completely.

for x in range(1, 21):
    if x == 13: #we need colon here because we are using an if statement. The if statement is used to execute a block of code if the condition is met. In this case, if x is equal to 13, then we will skip the current iteration of the loop and move on to the next iteration.
        continue
    else : #we need colon here because we are using an else statement. The else statement is used to execute a block of code if the condition is not met. In this case, if x is not equal to 13, then we will print x.
        print(x)

#this program will print the numbers from 1 to 20, but it will skip the number 13. The continue statement is used to skip the current iteration of the loop and move on to the next iteration. The break statement is used to exit the loop completely. In this case, we are using the continue statement to skip the number 13 and move on to the next iteration of the loop.