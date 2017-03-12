# **********---- Sets
print("# **********---- Sets  \n")


# A set is an unordered collection with no duplicate elements.
# Set objects also support mathematical operations like union, intersection, difference, and symmetric difference.
# Curly braces or the set() function can be used to create sets.
# Note: to create an empty set you have to use set(), not {};

basket = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
print(basket)                      # show that duplicates have been removed
print('orange' in basket)                 # fast membership testing)
print('\n' * 2)

# Demonstrate set operations on unique letters from two words
a = set('abracadabra')              # set initialization using set()
b = set('alacazam')
print('a is: ', a)
print("b is:  ", b)
print("letters in a but not in b: ", a - b)                 # letters in a but not in b
print("letters in either a or b: ", a | b)                  # letters in either a or b
print("letters in both a and b: ", a & b)                   # letters in both a and b
print("letters in a or b but not both: ", a ^ b)            # letters in a or b but not both
print('\n' * 2)


# **********---- Similarly to list comprehensions, set comprehensions are also supported
print("**********---- Similarly to list comprehensions, set comprehensions are also supported")
a = {x for x in 'abracadabra' if x not in 'abc'}
print("a is: ", a)
