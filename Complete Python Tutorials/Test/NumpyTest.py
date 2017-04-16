import numpy as vin

list = [2, 4, 5, 6, 7, 8, 8]
ar = vin.array(list)
print(ar)

list2 = ['hi', 23, "how", "teja"]
ar2 = vin.array(list2).reshape(2, 2)
print(ar2)

tup = (14, -3.98, 5+7j)
print(tup*2)
ar3 = vin.array(tup)
print(ar3)

random = vin.arange(10)
print(random)
print(random.size)
print(len(random))

random2 = vin.arange(0, 40, 3)
print(random2)

random3 = vin.arange(0, 40, step=5)
print(random3)

random4 = vin.arange(80, step=10)
print(random4)

print(vin.arange(80, step=10).size)

# linspace()
# zeros()
# ones()
# numpy datatype

print(vin.linspace(5, 15, 5))
lin = vin.linspace(5, 15, 5, retstep= True) # returns 2 set values 2nd set is set interval
print(lin)
print(lin[1]) # returns 2nd set interval of the linspace

print(vin.zeros(4))
print(vin.ones(4))
print(vin.zeros((2, 5, 4)))


my_vector = vin.array([34,6,74,3,68,9,0])
print(my_vector)
print(my_vector[4])
my_vector[3] = 43
print(my_vector)
x = my_vector[103%5]
print(x)
x = my_vector[my_vector.size%5]
print(x)

array2d = vin.arange(35)
array2d.shape = (7,5)
print(array2d)
print("\n",array2d[3])
print("\n",array2d[-2])
print(array2d[5,2])
row = 5
col = 2
print(array2d[row,col])
array3d = vin.arange(70)
array3d.shape = (2,7,5)
print(array3d)
print(array3d[1])
print(array3d[1][3])
print(array3d[1][3][2])
array3d[1][3][2] = 1007
print(array3d)



