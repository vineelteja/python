# **********---- Input and Output
# There are more than one way to get the output, one of the common way is using print() statement
# we can as well save the output in files, Let us learn how to do that in this chapter

# **********---- Fancier Output Formatting
# how do you convert values to strings? Luckily, Python has ways to convert any value to a string:
# pass it to the repr() or str() functions.
# The str() function is meant to return representations of values which are fairly human-readable
# repr() is meant to generate representations which can be read by the interpreter
# For objects which don’t have a particular representation for human consumption,
# str() will return the same value as repr(). Many values, such as numbers or structures like lists and
# dictionaries, have the same representation using either function. Strings, in particular, have two distinct
# representations.
s = 'Hello, world'
print("By using str()", str(s))
print("\nBy using repr()", repr(s))
print("\n"*2)


# Here are two ways to write a table of squares and cubes:
print("Here are two ways to write a table of squares and cubes:")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x).rjust(4))
    # rjust(z) creates z digits padding and start filling the information from right(called right justification)
print("\n")
print("If the output value is too long than rjust(z), then change z to length of largest value and spaces you needed")
for x in range(1, 11):
    print(repr(x).rjust(2), repr(x*x).rjust(3), repr(x*x*x*x*x*x).rjust(7))
    # if the output value is too long than rjust(z), then change z to length of largest value and spaces you needed
print("\n"*2)
# This example demonstrates the str.rjust() method of string objects, which right-justifies a string in a field of a
# given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center().
# These methods do not write anything, they just return a new string. If the input string is too long,
# they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually
# better than the alternative, which would be lying about a value. (If you really want truncation you can always
# add a slice operation, as in x.ljust(n)[:n].)


# **********---- .format() Working
# .format() one of the common formatting function to display our output clean
# for Example lets initialize 3 variables
one, two, three = 10, 20, 30
# lets see different ways of printing them
print(".format() one of the common formatting function to display our output clean")
print("Basic way: \n {} {} {}".format("I", "am", "Jarvis"))
print('Basic way: {0} and {1}'.format('Hello', 'World'))            # use according to position
print('Basic way: {1} and {0}'.format('Hello', 'World'))            # use according to position
print("First way: \n", one, two, three)
print("Second way: \n {} {} {}".format(one, two, three))                  # Positional placements
print("Third way: \n {one} {two} {three}".format(one=10, two='20', three='30'))
print("Third way: \n {} {two} {three}".format(one, two='20', three='30'))     # Positional & keyword arguments combined
# '!a' (apply ascii()), '!s' (apply str()) and '!r' (apply repr()) can be used to convert the value before its formatted
print("\nConverting to ascii, str, repr way: \n {!a} {!s} {!r}".format("I", "am", "Jarvis"))


# Lets use .format to write a table of squares and cubes:
print("\nHere are two ways to write a table of squares and cubes:")
for x in range(1, 11):
    print('{0:2d}{1:4d}{2:5d}'.format(x, x*x, x*x*x))           # {positional args : padding&type} is specified
    # An optional ':' and format specifier can follow the field name.
    # This allows greater control over how the value is formatted.
    # The  example formats values to 2, 4, 5 places.
print("\n"*2)


# **********----  Formating Dictionaries
# Passing an integer after the ':' will cause that field to be a minimum number of characters wide.
# This is useful for making tables pretty. Example
print("Passing an integer after the ':' will cause that field to be a minimum number of characters wide.")
table = {'Sjoerd': 4127, 'Jack': 4098, 'Dcab': 7678}            # Dictionary
for name, phone in table.items():
    print('{:10} ==> {:10d}'.format(name, phone))
print("\n"*2)


# If you have a really long format string that you don’t want to split up, it would be nice if you could reference
# the variables to be formatted by name instead of by position. This can be done by simply passing the dict and
# using square brackets '[]' to access the keys
print("Formatting Dict() using square brackets '[]' to access the keys")
table = {'one': 10, 'two': 20, 'three': 30}
print('one: {0[one]:d}; two: {0[two]:d}; '
      'three: {0[three]:d}'.format(table))
# This could also be done by passing the table as keyword arguments with the ‘**’ notation.
print("\nFormatting Dict() using keyword arguments with the ‘**’ notation.")
table = {'one': 10, 'two': 20, 'three': 30}
print('One: {one:d}; Two: {two:d}; Three: {three:d}'.format(**table))
print("\n"*2)


# There is another method, str.zfill(), which pads a numeric string on the left with zeros.
# It understands about plus and minus signs:
z = '12'.zfill(5)
print("Using zfill(): ", z)
z = '-3.14'.zfill(7)
print("Using zfill(): ", z)
z = '3.14159265359'.zfill(5)
print("Using zfill(): ", z)

# **********---- Old string formatting
import math
print('The value of PI is approximately %5.3f.' % math.pi)


