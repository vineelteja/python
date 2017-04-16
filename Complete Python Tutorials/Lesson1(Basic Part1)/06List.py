
# **********---- LIST
print("# **********---- LIST  \n")


# List is a basic data structure to store various data
# List is stored in '[ ]'
# when ever you see something inside [ ], recognize it as a list in python
funList = ["list", "can", "store", "anything", "numbers", 9, 99, 999,
           "can store even lists", [1, 2, 3], "objects", "etc"]


# List values can be retrieved using indexes.
# Length of the list is equal to Number of items in the list
# Index of the list always starts from 0
print("Retrieving elements")
print(funList[0])       # First item in the list is retrieved
# Lets get the 3rd element in the list that is "store" then
print(funList[3])    # This will give the 4th element because list starts from 0
print(funList[2])   # This will give the 3td element.
print(funList[2:5])     # Get a slice of elements
print('\n' * 2)
# to retrieve an item at position N the index value is N-1.


# There are various operations you can perform on lists, there are various
# inbuilt methods in python to manipulate the lists
# New List
listFun = ["this", "is", "new", "list"]


# **********---- Add new items in the list.append(element)
print("# **********---- Add new items in the list.append(element)")
listFun.append("new Item")


# Print the list to check
print(listFun)
print('\n' * 2)


# **********---- list.append(element)
# You can append list to the existing list
print("# **********---- list.append(element)")
listFun.append(funList)
print(listFun)
print('\n' * 2)

# **********---- list.extend(list)
# But this method forms a nested list, the solution to append the elements
# but not as a nested list is list.extend(list)
print("# **********---- list.extend(list)")
listFun.extend(funList)
print(listFun)
print('\n' * 2)


# **********---- list.insert(index, element) you can insert an element at a given index list.insert(index,element)
print("# **********----list.insert(index, element)")
listFun.insert(2, "Inserted")
print(listFun)
print('\n' * 2)


# **********---- list.remove(element)
# To remove an element from list list.remove(element)
print("# **********---- list.remove(element)")
listFun.remove(funList)     # funList is removed from listFun
print(listFun)
print('\n' * 2)


# **********----list.pop(index)
# Remove the item at the given position in the list, and return it.
# If no index is specified, a.pop() removes and returns the last item in the list.
print("# **********----list.pop(index)")
print(listFun.pop(-3))      # Traverse the list from back with negative indexes, starts from -1
print(listFun.pop())
print(listFun)
print('\n' * 2)


# **********---- list.index(element)
# To find out the index of a particular element
print("# **********---- list.index(element)")
print("New found at index ", listFun.index('new'))
print("New found in between index 2, 6", listFun.index('new',2,6))     # list.index(element, search from specified start index, to this index)
# Raises an error if the element is not found between the specified start to end index
print('\n' * 2)
# print(listFun.index('Mew'))       # Raises an error if the element is not found


# **********---- list.count(element)
# Returns how many times the element is repeated in the list
print("# **********---- list.count(element)")
print("Found the element", listFun.count('list'), "times")
print('\n' * 2)

numList = [23, 23, 5, 78, 9, 2, 3, 5, 8, 0, 9, 8654, 323, 456, 7]

# **********---- list.sort()
print("# **********---- list.sort()")
numList.sort()      # Sorts the list, returns an error if used when the list consists of int and str
print("Sorted list")
print(numList)
print('\n' * 2)

# **********---- list.reverse()  Reverses the list
print("# **********---- list.reverse()  Reverses the list")
numList.reverse()
print("Reversed list")
print(numList)
print('\n' * 2)


# **********---- list.copy()
# Copy the list
print("# **********---- list.copy()")
x = numList.copy()
print("numList is copied to x")
print(x)
print('\n' * 2)


# **********---- del()
# del works same as pop but del function will not return any value
print("# **********---- list.del()")
print("numList: ", numList)
del numList[0]
print("numList[0] is deleted", numList)
print("numList[2:7] is: ", numList[2:7])
del numList[2:7]                                 # delete a slice of elements
print("numList[2:7] is deleted", numList)
del numList[:]                                  # delete entire list
print("deleted entire list: ", numList)
print('\n' * 2)


# del can also be used to delete entire variables:
print("del() can also be used to delete entire variables:")
a = 10
print("a is :", a)
del a
# print("a is :", a)              # produces an error, as del removed it,  until again reinitialize it
print('\n' * 2)


# **********---- list.clear()
# Empties the entire list

print("# **********---- list.clear()")
listFun.clear()
print(listFun)
print('\n' * 2)