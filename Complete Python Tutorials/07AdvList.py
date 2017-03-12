# **********---- List as Stack
# Stack is a data structure, where first element retrieved at last or last element retrieved first
# To implement this in python use List
print("# **********---- List as Stack")
stack = [3, 45, 6, 77, 8]
print("Stack is \n",stack)
stack.append(98)            # pushes an element at the end of the list
print("Pusn elements to stack \n", stack)
stack.pop()                 # pops an element from the end of the list
print("Pop elements from stack \n", stack)
print('\n' * 2)


# **********---- List as Queues
# Queues are Data structures where the first element comes out first and last element comes out last
# To implement this in python using list and collections
# It is also possible to use a list as a queue, where the first element added is the first element
# retrieved (“first-in, first-out”); however, lists are not efficient for this purpose.
# While appends and pops from the end of list are fast, doing inserts or pops from the beginning
# of a list is slow (because all of the other elements have to be shifted by one).
print("# **********---- List as Queues")
que = ["I", "am", "first", "last", "element"]
from collections import deque               # Using in built classes,
queue = deque(que)                          # passing list to collections
queue.append("new")                         # adds an element to the end of the queue
print("queue is: ", queue)
print("element popped is: ", queue.popleft())                      # pops and element from the beginning
print("queue is: ", queue)
print('\n' * 2)


# **********---- In general
# An example to store a list of square numbers
print("# **********---- In general Example")
square = []
for x in range(10):
    square.append(x**2)
print("squar numbers range 10: ", square)
print('\n' * 2)


# **********---- List Comprehensions
# List has many in built functions to manipulate but if you need more custom values
# we will use list comprehension to solve the above example
print("# **********---- List Comprehensions")
squares = [x**2 for x in range(10)]
# How comprehension works is square brackets [expression for variable in list condition]
print("squar numbers range 10 using list comprehension:", squares)
print('\n' * 2)


# **********---- New example
# A list comprehension consists of brackets containing an expression followed by a for clause,
# then zero or more for or if clauses.
# The result will be a new list resulting from evaluating the expression in the context of the
# for and if clauses which follow it.
print("# **********---- New example")
example = [(x, y) for x in [1, 2, 3] for y in [3, 1, 4] if x != y]
#         [expression for clauses for clauses  condition] result is a list
print(example)

# This is equivalent to
examples = []
for x in [1,2,3]:
    for y in [3, 1, 4]:
        if x != y:
            examples.append((x, y))
print("Equivalent example: ", examples)
print('\n' * 2)

# **********---- Examples
# create a new list with the values doubled
x = [-4, -2, 0, 2, 4]
valDouble = [x*2 for x in x]
print("list with the values doubled: ", valDouble)
print('\n' * 2)

# filter the list to exclude negative numbers
exclude = [x*2 for x in x if x>0]
print("Filter the list to exclude negative numbers: ", exclude)
print('\n' * 2)

# apply a function to all the elements
fun = [abs(x*2) for x in x]
print("Applying a function to all the elements: ", fun)
print('\n' * 2)

# call a method on each element
freshfruit = ['  banana', '  loganberry ', 'passion fruit  ']
callMethod = [weapon.strip() for weapon in freshfruit]
print("call a method on each element: ", callMethod)
print('\n' * 2)

# create a list of 2-tuples like (number, square)
tupSquare = [(x, x**2) for x in range(5)]
print("create a list of 2-tuples like (number, square): ", tupSquare)
print('\n' * 2)

# flatten a list using a listcomp with two 'for'
vec = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
flat = [each for x in vec for each in x]
print("flatten a list using a listcomp with two 'for': ", flat)
print('\n' * 2)

# List comprehension can contain complex expressions and nested functions
from math import pi
complexNum = [str(round(pi, i)) for i in range(1, 6)]
print("Result of comprehension contain complex expressions and nested functions: ", complexNum)
print('\n' * 2)

# **********---- Nested List Comprehensions
# we can have a list comprehension in the place of an expression, check this
matrix = [
        [1, 2, 3, 4],
        [5, 6, 7, 8],
        [9, 10, 11, 12]
    ]
ca = [[row[i] for row in matrix] for i in range(4)]
#    [[express for clause in matrix] for clause in range]
#    [[this itself is expression] for clause in range]
# first range is stored in i, then inner list comprehension starts executing
# row[outer result] from matrix
print("# **********---- Nested List Comprehensions")
print("transpose rows and columns", ca)
print('\n' * 2)

# **********---- Break Down of the above example
transposed = []
for i in range(4):
    transposed.append([row[i] for row in matrix])
print("Break down of transpose rows and columns", transposed)
print('\n' * 2)


# **********---- Further Break Down of the above example
transposed = []
for i in range(4):
# the following 3 lines implement the nested listcomp
    transposed_row = []
    for row in matrix:
        transposed_row.append(row[i])
    transposed.append(transposed_row)
print("Further Break down of transpose rows and columns", transposed)
print('\n' * 2)


# **********---- Zip function
# In the real world, you should prefer built-in functions to complex flow statements.
# The zip() function would do a great job for this use case:
print("# **********---- Zip function does the same job effectively")
print(list(zip(*matrix)))
print('\n' * 2)


