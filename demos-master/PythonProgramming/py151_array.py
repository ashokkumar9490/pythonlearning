from array import *

array1 = array('i', [10, 120, 30, 140, 50])     # "10"
# print(array1)


# for x in array1:
#     print(x, end=",")

# print()

# friends = ["friend1", "friend2", "friend3"]
# print(friends)
# print(",".join(friends))

# # print array1 elements separated by comma
# print()
# print(array1.tolist())
# print(",".join(map(str, array1)))


# print(array1.typecode)
# print(array1.itemsize)          # size of each item in bytes

# print(array1)
# array1.append(60)
# print(array1)
# array1.insert(1, 70)
# print(array1)
# array1.remove(140)
# print(array1)
# i2 = array1.pop(2)       # Removes item i from the array and returns it
# print(i2)

# array1.reverse()
# print(array1)

# # Returns the index of the first occurrence or error if not found
# ind = array1.index(50)
# print(ind)

# sort the array  (sort vs sorted)

print(array1)
# l1 = sorted(array1)     # returns a list
# print(l1)
# print(type(l1))


# converted default list to array of type int
array1 = array('i', sorted(array1))
print(array1)
print(array1.typecode)
