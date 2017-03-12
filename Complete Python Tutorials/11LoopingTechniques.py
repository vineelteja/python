# **********---- Looping Techniques
# It is sometimes tempting to change a list while you are looping over it;
# however, it is often simpler and safer to create a new list instead.
print("**********---- Looping Techniques")
import math
raw_data = [56.2, float('NaN'), 51.7, 55.3, 52.5, float('NaN'), 47.8]
filtered_data = []
for value in raw_data:
    if not math.isnan(value):
        filtered_data.append(value)
print("New list: ",filtered_data)
print("\n"*2)


# **********---- Reversed
print("**********---- Reversed")
fun = [21, 33, 44, 55, 77, 77, 99]
print("Before Reverse ", fun)
fun = reversed(fun)                                 # reversed is a in built method to reverse the values
print("Applying Reverse ", list(fun))
print("\n"*2)

# **********---- Applying reversed for range
# To loop over a sequence in reverse, first specify the sequence in a forward direction
# and then call the reversed() function.
print("**********---- Appying reversed for range")
for i in reversed(range(1, 10, 2)):                 # reversed is a in built method to reverse the values
    print(i)
print("\n"*2)


# **********---- Appying Sorted
# Use the sorted() function which returns a new sorted list while leaving the source unaltered.
print("**********---- Appying Sorted")
basket = ['apple', 'orange', 'apple', 'pear', 'orange', 'banana']
print("Before Sorted: ", basket)
print("After Sorted: ", sorted(basket))
num = [23, 5, 689, 8764, 32, 345, 6, 78, 76, 5432]
print("\nBefore Sorted: ", num)
print("After Sorted: ", sorted(num))
print("\n"*2)


# **********---- Appying Sorted in loops
print("**********---- Appying Sorted in loops")
for f in sorted(basket):
    print(f)
print("\nTo remove duplicates use set")
for f in sorted(set(basket)):
    print(f)
print("\n" * 2)
