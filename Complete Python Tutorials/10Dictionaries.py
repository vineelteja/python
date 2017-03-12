# **********---- Dictionaries
print("# **********---- Dictionaries  \n")

# Dictionaries are {key:value, key:value, key:value} pairs separated with comma.
# Immutable data Strings, Number, Tuples can be used as key
# Unlike indexing in list, data can be accessed using keys
# The main operations on a dictionary are storing a value with some key and extracting the value given the key
# It is also possible to delete a key:value pair with del
# If you store using a key that is already in use, the old value associated with that key is forgotten
# It is an error to extract a value using a non-existent key.
tel = {}                                        # initializing empty dictionary
tel = {'jack': 4098, 'sape': 4139}              # Dictionary with key:value pairs
tel['guido'] = 4127                             # Adding a tel[key] = value to the dictionary
print("Dictionary after adding a key:value pair: ", tel)
print('\n' * 2)

# **********---- dict() constructor
# dict() constructor builds dictionaries directly from sequences of key-value pairs
print("dict() constructor builds dictionaries directly from sequences of key-value pairs")
fun = dict([('sape', 4139), ('guido', 4127), ('jack', 4098)])
print("Dictionaries using dict()", fun)
print('\n' * 2)


# **********----  Dictionary comprehensions
# Dict comprehensions can be used to create dictionaries from arbitrary key and value expression
print("**********----  Dictionary comprehensions")
funComp = {x: x**2 for x in (2, 4, 6)}
print("Dictionaries using comprehension: ", funComp)
print('\n' * 2)


# **********---- key:value pairs using keyword arguments:
# When the keys are simple strings, it is sometimes easier to specify pairs using keyword arguments:
print("**********---- key:value pairs using keyword arguments:")
fun = dict(sape=4139, guido=4127, jack=4098)
print("Dict using Keyword args: ", fun)
print('\n' * 2)


# **********---- Using Loop and Zip() Function
# To loop over two or more sequences at the same time, the entries can be paired with the zip() function.
questions = ['name', 'gender', 'favorite color']
answers = ['lancelot', 'male', 'blue']
fun = {}
for q, a in zip(questions, answers):
    fun[q] = a
print("Dictionary using list, loop and zip() \n", fun)
print('\n' * 2)


# Deleting a key value pair
print("Deleting a key value pair")
del tel['sape']                                 # del tel[key] deletes the key value pair associated with the key
print("Dictionary after using del ", tel)
tel['irv'] = 4127                               # Adding a tel[key] = value to the dictionary
print("Dictionary after adding a key:value pair: ", tel)
print('\n' * 2)


# **********---- List(dict.key())
# lists all the keys from the dictionary
print("lists all the keys from the dictionary")
print("List of keys from dictionary tel: ", list(tel.keys()))
print('\n' * 2)


# **********---- sorted(dict.key())
# list the keys in a sorted order
print("list the keys in a sorted order")
print("List of sorted keys from dictionary tel: ", sorted(tel.keys()))
print('\n' * 2)


# **********---- searching for values using in and not in
print("searching for values using in and not in")
x = 'guido' in tel
print("'guido' in tel", x)
x = 'jack' not in tel
print("'jack' not in tel", x)
print('\n' * 2)


# **********---- Looping Techniques
# using Loops Key and values can be retrieved at the same time
fun = dict(sape=4139, guido=4127, jack=4098)
for k, v in fun.items():
    print("key: ", k, "  value:", v)
print('\n' * 2)


# **********---- Sequencing using enumerate and dictionary
# When looping through a sequence, the position index and corresponding
# value can be retrieved at the same time using the enumerate() function.
print("No Value")
for i, v in enumerate(['tic', 'tac', 'toe']):
    print(i, v)
print('\n' * 2)


