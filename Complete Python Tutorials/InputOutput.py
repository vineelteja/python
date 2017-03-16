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
    print(repr(x).rjust(2), repr(x*x).rjust(3), end=' ')
    # Note use of 'end' on previous line
    print(repr(x*x*x).rjust(4))
print("\n" * 2)

print("Here are two ways to write a table of squares and cubes:")
for x in range(1, 11):
    print('{0:2d} {1:3d} {2:4d}'.format(x, x*x, x*x*x))
print("\n"*2)
# This example demonstrates the str.rjust() method of string objects, which right-justifies a string in a field of a
# given width by padding it with spaces on the left. There are similar methods str.ljust() and str.center().
# These methods do not write anything, they just return a new string. If the input string is too long,
# they don’t truncate it, but return it unchanged; this will mess up your column lay-out but that’s usually
# better than the alternative, which would be lying about a value. (If you really want truncation you can always
# add a slice operation, as in x.ljust(n)[:n].)

# There is another method, str.zfill(), which pads a numeric string on the left with zeros.
# It understands about plus and minus signs:
z = '12'.zfill(5)
print("Using zfill(): ", z)
z ='-3.14'.zfill(7)
print("Using zfill(): ", z)
z = '3.14159265359'.zfill(5)
print("Using zfill(): ", z)
