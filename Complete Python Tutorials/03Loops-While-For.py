                ########## Loops in Python
# while Loop
# for Loop


                ########## While loop
# printing 10 numbers using while loop
i = 0                       # create a variable i with value of 0
while(i < 10):              # check if value of i is less than 10 if true, statements inside while are executed. if flase, do not enter the loop
    i += 1                  # add 1 to the value of i and store back in i
    print(i)                # print the value of i, and go back to while statement and repeate the process till the conditin is false

# Simple implementation of while loop
# Show first 10 fibonacci numbers from 0
# What is fibonacci Numbers
# starting from 1 add the number to the previous number then the result is fibonacci series
# Result should be  0,1,1,2,3,5,8,13

a, b = 0, 1                         # initialize a and b to 0 and 1
while(a <= 30):                     # check the value of a is less equal to 30, if true execute block inside while
    a, b = b, b + a                 # Value of b is stored in a, and value of b + a is stored in b
    print(a)                        # print the value of a, this happens till the condition of the loop is false

                ########## For in loop
# For loop is used to traverse(go to and fro) through the Sequence like list, strings etc.
x = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0]      # x is a variable, of type list
for num in x:                           # num is a variable which stores one value from x in each iteration(loop)
    print(num)                          # Printing that value of num to the console

                # ********** break and continue
# two important keywords we use in loops to manipulate loops are

# break is used to stop the loop
# continue is used to skip iteration (skip one loop)

# Using break
print("break")
for num in range(10):
    print(num)                         # This loop will print only till 5
    if (num == 5):
        break

# Using continue
print("Continue")
for num in range(10):
    if (num == 5):
        continue
    print(num)                         # This loop will not print 5, because it is skipped

                # ********** pass keyword
# Pass statement does nothing, it just make things easy when you don't know what to have as a block of code
# example

def functionName():                                 # Compiler will return error if there is no body to the function
    pass                                            # That kind of situation can be handled by using pass

class Name:                                         # Compiler will return error if there is no  to the class
    pass                                            # That kind of situation can be handled by using pass

if (9 != 10):                                       # Compiler will return error if there is no body to the function
    pass                                            # That kind of situation can be handled by using pass


