import numpy as np
from numpy import random


# arr = np.arange(1, 50, 10)
# print(arr)
# print(arr.sum())

# sarr = -np.sort(-arr)
# print(sarr)


# arr1 = random.randint(low=50, high=80, size=20, dtype=int)
# print(arr1)


# arr2 = np.linspace(10, 20, 25)  # including high
# print(arr2)


# arr3 = np.arange(25).reshape(5, 5)
# print(arr3)


arr4 = np.array([[0, 1, 2, 3], [5, 6, 7, 8], [9, 10, 11, 12]])
farr4 = arr4.flatten()
print(farr4)
arr4[1, 1] = 11
print(arr4)
print(farr4)


# rarr4 = arr4.ravel()
# print(rarr4)

# arr4[1, 1] = 11
# print(arr4)
# print(rarr4)

# sel_arr4_g5 = (arr4 > 5)
# print(sel_arr4_g5)
# print(arr4[sel_arr4_g5])
