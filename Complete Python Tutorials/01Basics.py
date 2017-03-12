"""
Hi I am Vineel Teja,
I have completed my Masters Degree from International Technological University, San Jose, California.

I am sharing my knowledge of python as much as I can with you.
This is My Python Repository in GitHub
I am going to Start from the Basics to Data Structures in as much as detail as possible.
"""


# Lesson 1  '#' symbol is used to comment the code, such as this line. This line is a comment line.
# Comment lines are ignored by interpreter


# **********----Variables in Python----**********
# A variable is a room in your house to hold Values
# Values can be of any type ranging from Numbers, characters, strings etc.
# RULES TO DECLARE A VARIABLE
# variable = value. This is how you generally declare the variable
# You can declare a variable directly just by
# Assigning a value to an english alphabet or
# A word or
# A word which starts with '_'
# for example


a = 10                              # This is a Number/Integer
air = 'I'                           # This is a character, should always surround the value in single quotes
A = "eleven"                        # This is a string, should always surround the value in single / double quotes
_water = [10, 'I', "eleven"]        # This is a list


# Point to remember
# In python A = "eleven" is different from a = 10,
# Python is case sensitive language. so always remember what kind of variable you are using

# **********----End of Variable----**********

# **********----Print to console----**********
# Python uses console to produce the output, so to show things on console we have to use print()
# To output your name or a string you have to surround the string in double quotes in the print


print("Hello World")


# I have declared a, air, A, _water above, but to know what type of value the
# variable is holding we have to use - type()


print("Type of a is: ", type(a))
print("Type of air is", type(air))
print("Type of A is", type(A))
print("Type of _water is", type(_water))

# **********----Operators----**********
# **********---- Arithmetic Operators


print("1+1 is:", 1+1)                                                          # Add 2 numbers with +
print("Add me to"+" New string")                                               # Join 2 Strings with +
print("2-2 is:", 2-2)                                                          # Subtract 2 numbers with -
print("2*2 is:", 2*2)                                                          # Multiply 2 numbers with *
print("8/2 is:", 8/2)                                                          # Divide 2 numbers with / for Quotient
print("13%3 is:", 13 % 3)                                                        # divide 2 numbers with % for Remainder
print("3**4 is:", 3**4)                                                        # 3 raised to the power of 4 with **
print("25//4 is:", 25//4)                                                      # for quotient without decimal


# **********---- Logical Operators


print("Check if 2 == 2 ", 2 == 2)
# gives True - Compare if 2 values are equal
print("Check if 2 != 23 ", 2 != 23)
# gives True - Compare if 2 values are not equal
print("Check if 3 < 5 ", 3 < 5)
# gives True - Compare if 1st values is smaller
print("Check if 5 > 3 ", 5 > 3)
# gives True - Compare if 1st value is greater
print("Check if 3 <= 5 ", 3 <= 5)
# gives True - Compare if 1st values is smaller or equal
print("Check if 5 >= 3 ", 5 >= 3)
# gives True - Compare if 1st value is greater or equal

# **********---- Assignment Operators

x = 10                                                              # Assign 10 to x
print("Value of x after x = 10 is ", x)
x += 10                                                             # add 10 to the value of x
print("Value of x after x += 10 is ", x)
x -= 10                                                             # Subtract 10 from the value of x
print("Value of x after x -= 10 is ", x)
x *= 10                                                             # Multiply 10 to x
print("Value of x after x *= 10 is ", x)
x **= 10                                                            # Raise X to 10
print("Value of x after x **= 10 is ", x)
x //= 10                                                            # Performs floor division and assign to x
print("Value of x after x //= 10 is ", x)

# **********---- Logical Operators

a and air
# and is a keyword, can be used to check conditions. all operands has to be true for the result to be true

air or a
# or is a keyword, can be used to check conditions. any one of operand has to be true for the result to be true

not(air or a)
# reverse the result of the condition


# **********---- Membership Operators

a = [1, 2, 3, 4, 5]
# a is a list of numbers

b = 2 in a
# in returns true or false, in this case 2 is in a, so it returns true

c = 7 not in a
# not in returns true or false, in this case 7 is not in a, so it returns false


# **********---- Basic Method/Functions
# Functions is a block of code, which can be used to reuse a part of code
# In python Function can be defined starting with 'def' keyword
# Syntax for definition of Method/Function is def functionName(parameters):
# on next line give indentation and write the code to be executed
# Syntax for calling the Method/Function is functionName(parameters).


def function_name():                                 # Defining a function
    print("I am printing inside a function")        # Body of the function
function_name()                                      # calling a function


def name_function(parameter):               # This function takes a parameter(beauty of python,
                                            # This parameter can be anything a number, string, list, object etc)
    print("I am a function with only 1", parameter)  # That parameter is printing at the end of the print statement
name_function("parameter")                           # A string is being passed to the function as a parameter.

# **********---- Strings and Lists

# **********---- Strings JUST INTRODUCTION
# anything surrounded in double quotes is a string
# "afadjfl323423(*)(dfaf?" even though that is gibberish, python takes it as a string

name = "qwe123!@#${}"                           # This is a string

# Python has a built-in string class named "str".
# This string class has many in built functions. like finding the length of the string etc.

print("length of variable name is: ", len(name))

# There are various String Methods to manipulate strings, You will love it, lets discuss in later.

# **********---- LIST JUST INTRODUCTION
# List is a basic data structure to store various data
# list is stored in '[ ]'

funList = ["List", "can", "store", "anything", "numbers", 9, 99, 999,
           "can store even lists", [1, 2, 3], "objects", "etc"]

# when ever you see something inside [ ], recognize it as a list in python
# This list has many in built functions. like finding the length of the list etc.

print("length of list funList is: ", len(funList))
