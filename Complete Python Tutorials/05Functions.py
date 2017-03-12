                ########## Basic Method/Functions
# Functions is a block of code, which can be reused a part of code in other places of the project
# In python Function can be defined starting with 'def' keyword
# Syntax for definition of Method/Function is def functionName(arguments): on next line give indentation and write the code to be executed
# Syntax for calling the Method/Function is functionName(arguments).


# Procedure and Function
# Procedure and Function are almost same in terms of syntax and functionality.
# Procedure is a block of code which does not return any value.
# Function is a block of code which returns a value


# def functionName():                                 # Defining a function
#     print("I am printing inside a function")        # Body of the function
# functionName()                                      # calling a function
print('\n' * 2)
def nameFun():                                          # This is a function with no arguments
    print("I am a function with no arguments")
nameFun()                                               # This statement is used to call the function

def nameFunction(arguments):                            # This function takes a arguments(beauty of python, This arguments can be anything a number, string, list, object etc) This arguments are called as formal arguments
    print("I am a function with only 1", arguments)     # That arguments is printing at the end of the print statement
nameFunction("argument")                                # A string is being passed to the function as a arguments. This arguments are called as actual arguments

# Even though the function above does not return any value it is not a procedure, because it still does return a value "None"
# try this
print('\n' * 2)
print("The value of a function with no return is: ", nameFunction(0))

# ********** Function using return keyword

print('\n' * 2)
def funFunction(name, time):                                # This function accepts 2 arguments, but there is a catch
    print("Hello {} the time is {}" .format(name, time))
funFunction("James", 9)                 # The first and second arg in the call must match the order in function definition

def funFunc(name, a, b):                # This function accepts 3 arguments
    res = a + b                         # if the values of a and b are not numbers compiler throws an error
    print("{} is carrying {} books with him".format(name, res))
funFunc("james", 1,3)                   # As long as you pass the arguments in the order, you program will execute.


# def funcFun(name, a, b):              # This function accepts 3 arguments
    # res = a + b                       # if the values of a and b are not numbers compiler throws an error
    # print("{} is carrying {} books with him".format(name, res))
# funcFun(1, 3, "James")                # As the arguments are not in order, you program will not execute, so I commented out




print('\n' * 2)
def funMath(a,b):                                            # returns Addition of 2 arguments
    result = a + b
    return result
print("This time a function returns a value ")
var = funMath(32, 45)                                        # Here we are passing 2 arguments
print("Adding 32 + 45: ", var)

print('\n' * 2)
def funNumbers(n):                          # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []                             # initializing list
    a, b = 0, 1
    while a < n:
        result.append(a)                    # adds the value to the list
        a, b = b, a+b
    return result
print("Returns a list of fibonacci series\n",funNumbers(100))                      # calls the function

# ********** Function with arguments
# There are three forms with variable number of arguments
# 1. Default Argument values
# 2. Keyword Arguments
# 3. Arbitrary Argument Lists


# 1. Using Default Argument values
print('\n' * 2)


def funMath(a=5, b=5):                # Here we are defining the default values of a and b
    result = a + b
    return result
print("Adding default values ",funMath())             # Even though we are not giving any arguments, the default values are initialized
print("\nif you specify the argument, the value overrides the default argument")
print("Adding values ",funMath(10,10))
print('\n' * 2)
def funNumbers(n = 50):                          # return Fibonacci series up to n
    """Return a list containing the Fibonacci series up to n."""
    result = []                             # initializing list
    a, b = 0, 1
    while a < n:
        result.append(a)                    # adds the value to the list
        a, b = b, a+b
    return result
print("Returns a list of fibonacci series by using default arguments\n",funNumbers())                      # calls the function
print("\nif you specify the argument, the value overrides the default argument\n",funNumbers(200))

# Important warning: The default value is evaluated only once.
# This makes a difference when the default is a mutable object such as a list, dictionary, or instances of most classes.
# For example, the following function accumulates the arguments passed to it on subsequent calls:


# 2. Keyword Arguments


# def funcFun(name, a, b):              # This function accepts 3 arguments
    # res = a + b                       # if the values of a and b are not numbers compiler throws an error
    # print("{} is carrying {} books with him".format(name, res))
# funcFun(1, 3, "James")                # As the arguments are not in order, you program will not execute, so I commented out

# as you know the above function will not work because the arguments are not in the order we can fix it with Keyword Arguments in python
print('\n' * 2)
def funcFun(name, a, b):              # This function accepts 3 arguments
    res = a + b                       # if the values of a and b are not numbers compiler throws an error
    print("{} is carrying {} books with him".format(name, res))
funcFun(b=3, a=1, name="James")                # As the arguments are not in order, you program will not execute, so I commented out

# Even though the arguments are not in order, we are specifying the arguments even in the function call
# We are calling the exact same variables used in the definition and assigning the values using assignment operator


# Note: If you are using keyword arguments, try to make sure you provide all keywords to all the arguments to avoid errors
# if you start the actual arguments using keyword argument you must specify keyword arguments for all the arguments.
# Positional arguments(arguments in order) always comes first and are followed by keyword arguments

# ********** use of *args(arguments) **kwargs(keyword arguments)
# *args

# At some point in your programming life, you might want to give a very lengthy number of arguments
# Instead of typing them all in function definition and function call, you can use *args
print('\n' * 2)
def funArguments(*anything):
    print("This function is talking many actual arguments, but just 1 formal argument")
    for each in anything:
        print(each)
funArguments(1,2,3,4,5,6,7,8,9,0)


# If you have saved your arguments as a list and you want to pass each element of the list
# as an argument for a function then this is the syntax.

# The process of pass each element of the list as an argument is called Unpacking Argument Lists

print('\n' * 2)
simpleList = ["hello", "I", "am", 1, "single", "list"]


def argsFunList(*anything):
    print("This function is talking one list as actual argument, and one formal argument")
    for each in anything:
        print(each)
argsFunList(*simpleList)                # the process of pass each element of the list as an argument is called Unpacking Argument Lists

# **kwargs
# At some point in your programming life, you might want to give and pass lengthy keyword arguments with values to function
# Instead of typing them all in function definition you can use **args

print('\n' * 2)


def funKeyArgs(**funkeyword):
    print("This function takes lengthy keyword arguments with values to function")
    for each in funkeyword:
        print(each,funkeyword[each])
funKeyArgs(name='james', age='25', planet='earth')

# lets combine everything

print('\n' * 2)
simpleBook = ["comic", "romance", "adventure"]
print("lets combine everything")


def crazyFunction(name='james', *books, **kwargs):
    print("His name is", name)
    for each in books:
        print(name, " reads ", each, "books")
    for each in kwargs:
        print(each,":", kwargs[each])
crazyFunction("pluto", *simpleBook,
              book="Ranger",
              author="tom",
              published=2020,
              rating=4.8
              )



# NOTE: Remember Positional arguments(arguments in order) always comes first and are followed by keyword arguments
#                           *args comes first and followed by **kwargs
# Anything after *args are always keyword arguments, all positional arguments will occur before *args


def concat(*args, sep="/"):
    return sep.join(args)
concat("earth", "mars", "venus")
concat("earth", "mars", "venus", sep=".")

# ********** Function Annotations
# Function Annotations completely optional metadata information,
# that are stored in  __annotations__ attribute of the function as a dictionary
print('\n' * 2)


def funcFun(name:str, a:int, b:int = 10):                # After each attribute we are specifying what data type an attribute is expecting, but it is you to pass the annotated data type during call
    res = a + b
    print("{} is carrying {} books with him".format(name, res))
funcFun(b=3, a=1.5, name="James")
print('\n' * 2)


def funcFun(name:str, a:int, b:int = 10) -> str:                # Here we are annotating what kind of return type the function is going to return  by uinsg "->" and the data type
    res = a + b
    print("Arguments: ", name, a, b)
    return "{} is carrying {} books with him".format(name, res)
print(funcFun(b=3, a=1.5, name="James"))
print("Annotations:", funcFun.__annotations__)

# Lets see how annotations are stored in a function
