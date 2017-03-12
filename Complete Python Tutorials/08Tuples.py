# **********---- Tuples
print("# **********---- Tuples  \n")

# Tuples are very similar to the lists, but
# Tuples are immutable, once a tuple is initialized, elements cannot be deleted or added or reassigned
# Nested tuples are possible
# Tuples are surrounded by "( )"
# Tuples are accessed just like lists via indexing.

funTuples = (1, 2, 3, 4, 5)
print("Tuples: \n",funTuples)
print('\n' * 2)

funTuples = (1, 2, 3, 4, 5, (1, 2, 3, 4, 5))
print("Nested Tuples: \n",funTuples)
print('\n' * 2)

a = 99, 98, 97
print(type(a), "a is an example of tuple packing, The values assigned to a are packed together in a tuple")

