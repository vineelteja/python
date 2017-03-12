                ########## Range Function
# Rang function generates array of numbers

x = range(5)                                         # x here stores 0,1,2,3,4. To print them use loop, Here Range takes a single argument
print("range(5) is")
for num in x:
    print(num)


# if you want to produce numbers from x to y

x = range(5, 10)                                     # x here stores 5, 6, 7, 8, 9  To print them use loop, Here Range takes a single argument
print("range(5, 10) is")
for num in x:
    print(num)

# if you want to iterate over a sequence
a = ['Mary', 'had', 'a', 'little', 'lamb']           # a is a list of strings
print("i is ")
for i in range(len(a)):                              # len(a) gives the length of list a i.e 5, so range(5) is 0,1,2,3,4. for each element of i in range(5)
    print(i, a[i])                                   # print value of i and element available at the position of i

