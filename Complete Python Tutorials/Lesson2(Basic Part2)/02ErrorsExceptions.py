# **********---- Syntax Errors
# Syntax errors, also known as parsing errors,
# while True print('Hello world')                   # Uncomment the line to findout the error


# **********---- Exceptions
# Even if a statement or expression is syntactically correct, it may cause an error when an attempt
# is made to execute it. Errors detected during execution are called exceptions

# 10 * (1/0)                        # Uncomment the line to findout the error


# 4 + spam*3                        # Uncomment the line to findout the error


# '2' + 2                           # Uncomment the line to findout the error

# You will know what kind of error you encountered, if you read the error produced by the interpreter carefully
# The interpreter mentions what kind of error it is types in the example are ZeroDivisionError, NameError and TypeError.


# **********---- Handling Exceptions
# An example how to handle exceptions
while True:
    try:
        x = int(input("Please enter a number: "))
        break
    except ValueError:
        print("Oops!  That was no valid number.  Try again...")
# This program will not crash even though the user dont gives a number, but shows a meaningful error and the program
# keeps on running
#
# The try statement works as follows.
    # First, the try block (the statement(s) between the try and except keywords) is executed.
    # If no exception occurs, the except block is skipped and execution of the try statement is finished.
    # If an exception occurs during execution of the try block, the rest of the block is skipped.
    # Then if its type matches the exception named after the except keyword, the except clause is executed,
    # and then execution continues after the try statement.
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

# The last except Block may omit the exception name(s), to serve as a wildcard.
# Use this with extreme caution, since it is easy to mask a real programming error in this way! It can also be used to
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

# Try... except can have an else statement at the end, the use of the else clause is better than adding additional code
# It is useful to raise an exception if try did not raise an exception For Example:
for arg in sys.argv[1:]:
    try:
        f = open(arg, 'r')
    except OSError:
        print('cannot open', arg)
    else:
        print(arg, 'has', len(f.readlines()), 'lines')
        f.close()
# When an exception occurs, it may have an associated value, also known as the exception’s argument.
# The presence and type of the argument depend on the exception type.

