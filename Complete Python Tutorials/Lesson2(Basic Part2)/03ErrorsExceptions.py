# **********---- Syntax Errors
# Syntax errors are those when you do not write the statement correctly, they are also known as parsing errors,
# These are like spelling mistakes in your program


# why and how to use Exceptions in your program
# To make sure your program or the software not to crash in the middle when the user is using it.
# when you thing a part of code needs a logical input either from the user or from different program, which when
# not received will crash your program, you can prevent this crash by using exceptions
# There are three parts in the Exception 'try', 'except', 'raise', 'finally'
# Please the piece of code which you think will give an error, in the try block
# Use except to do specific action when an error is produced by try block
# Use raise to raise your own exception
# What ever the situation is do everything which is in finally block


# while True print('Hello world')
# Uncomment the above line to find out the error, The mistake is we missed ':' after True


# **********---- Exceptions
# Even if a statement or expression is syntactically correct, it may cause an error when an attempt
# is made to execute it. Errors detected during execution are called exceptions

# 10 * (1/0)                        # Uncomment the line to findout the error, division by zero


# 4 + spam*3                        # Uncomment the line to findout the error, spam is  not defined befored it is used


# '2' + 2                           # Uncomment the line to findout the error, '2' is a string cannot add to a number

# You will know what kind of error you encountered, if you read the error produced by the interpreter carefully
# The interpreter mentions what kind of error it is types in the example are ZeroDivisionError, NameError and TypeError.


# **********---- Handling Exceptions
# An example how to handle exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except:
        print("Oops!  That was no valid number.  Try again...")
# This program will not crash even though the user do not gives a number as input,
    # but shows a meaningful error and the program keeps on running
# The try statement works as follows.
    # First, the try block (the statement(s) between the try and except keywords) is executed.
    # If no exception occurs, the except block is skipped and execution of the try statement is finished.
    # If an exception occurs during execution of the try block, the rest of the block is skipped.
    # Then if its type matches the exception named after the except keyword, the except clause is executed,
    # and then execution continues after the try statement. (when we define more than one except block)
    # If an exception occurs which does not match the exception named in the except block,
    # it is passed on to outer try statements; if no handler is found, it is an unhandled exception and execution stops
    # with a message as shown above.

# A try statement may have more than one except block, One handler is executed out of all
#  An except clause may name multiple exceptions as a parenthesized tuple, for example:
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
    except NameError:
        print("Oops! That was a Name error: Trying to access undefined variable")
    except (ValueError, NameError):
        print("ValueError and NameError")
    except:
        print("There is an error please check")
# The last except Block may omit the exception name(s), to serve as a wildcard.
# Use this with extreme caution, since it is easy to mask a real programming error in this way!


# User can create his one exceptions by inheriting from 'Exception' For example
class B(Exception):                         # Inheriting from Exception
    pass
class C(B):                                 # Inheriting from B
    pass
class D(C):                                 # Inheriting from C
    pass

for cls in [B, C, D]:
    try:
        raise cls()
    except D:                               # D is child of C, C is child of B, B is child of Exception.
        print("D")
    except C:                               # C is child of B, B is child of Exception.
        print("C")
    except B:                               # B is child of Exception. So all  D, C, B will act as exception clause
        print("B")
# Note that if the except clauses were reversed (with except B first), it would have printed B, B, B
# That's because C and D are children of B


# print an error message and then re-raise the exception (allowing a caller to handle the exception as well):
# for example
import sys

try:
    f = open('myfile.txt')
    s = f.readline()
    i = int(s.strip())
except OSError as err:
    print("OS error: {0}".format(err))
except ValueError:
    print("Could not convert data to an integer.")
except:
    print("Unexpected error:", sys.exc_info()[0])
    raise


# Try... except can have an else statement at the end,
# if the no except block is able to handle the error produced by try, it will be handled by else. Example
arg = "something"
try:
    f = open(arg, 'r')
except OSError:
    print('cannot open', arg)
else:
    print(arg, 'has', len(f.readlines()), 'lines')          # Because this is not an OSError else block is executed
    f.close()


# Exceptions may contain some values in terms of exception arguments.
# you can access these arguments using by creating a variable of that exception type using except Exception as variable
# __str__() is defined in every exception class to print down the arguments without having to reference .args.
try:
    raise Exception('spam', 'eggs')
except Exception as inst:
    print(type(inst))    # the exception instance
    print(inst.args)     # arguments stored in .args
    print(inst)          # __str__ allows args to be printed directly, but may be overridden in exception subclasses
    x, y = inst.args     # unpack args
    print('x =', x)
    print('y =', y)


# Exception
# s can also be used to handle functions just by calling it
def this_fails():
    x = 1/0
try:
    this_fails()                         # The error is caught in the try block even though it occurs in the function
except ZeroDivisionError as err:
    print('Handling run-time error:', err)


# **********---- Raising Exceptions
# raise will allow the programmer to create an exception out of no where
raise NameError('HiThere')


# If you are not sure about handling a specific error, and you still want to raise it again then just use raise keyword
# Uncomment these to try the code.
try:
    raise NameError('HiThere')
except NameError:
    print('An exception flew by!')
    raise


# **********---- User-defined Exceptions
# You can create your own exceptions by creating your own Class and inherit it from Exception
# You can allow your class to do anything, but try to keep simple, use limited attributes(variables) to store the info
# about the error.
# When creating a module to handle different kinds of exceptions, use one class to inherit from Exception which defines
# other user defined class exceptions in this module and let other classes to inherit from the base class.
# child classes specify exception for different error conditions:


class UserError(Exception):
    """Base class for exceptions in this module."""
    pass

class InputError(UserError):
    """Exception raised for errors in the input.

    Attributes:
        expression -- input expression in which the error occurred
        message -- explanation of the error
    """

    def __init__(self, expression, message):
        self.expression = expression
        self.message = message

class TransitionError(UserError):
    """Raised when an operation attempts a state transition that's not
    allowed.

    Attributes:
        previous -- state at beginning of transition
        next -- attempted new state
        message -- explanation of why the specific transition is not allowed
    """

    def __init__(self, previous, next, message):
        self.previous = previous
        self.next = next
        self.message = message
# Most exceptions are defined with names that end in “Error,” similar to the naming of the standard exceptions.
# Many standard modules define their own exceptions to report errors that may occur in functions they define.
# More information on classes is presented in chapter Classes.


# **********---- Defining Clean-up Actions (finally)
# What ever the situation is do everything which is in finally block,
# weather the try raises an exception or not execute the finally block.
try:
    raise KeyboardInterrupt
finally:
    print('Goodbye, world!')
# Note:
# In real world applications, the finally clause is useful for releasing external resources
# (such as files or network connections), regardless of whether the use of the resource was successful
# Such as to close the file at any cost.


# **********---- Predefined Clean-up Actions
# with block is used to close the action weather the action is complete or not,
# once the block is executed the action is closed.
# lets look at this example

for line in open("myfile.txt"):
    print(line, end="")
# In this code we are not specifing to close the file, so the file is left open for undetermined amount of time
# which will cause issues in later stages.
with open("myfile.txt") as f:
    for line in f:
        print(line, end="")
# once the execution of the with block is complete the file is closed automatically.
# even if a problem was encountered while processing the lines.
# Objects which, like files, provide predefined clean-up actions will indicate this in their documentation.
