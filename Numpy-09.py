# Splitting NumPy Arrays...
import numpy as np
array = np.array([1, 2, 3, 4, 5, 6])
arr = np.array_split(array, 3) #1.array name ... 2.number of splites
print(arr)
"""output:[array([1, 2]), array([3, 4]), array([5, 6])]""" 

# Split Into Arrays
print(arr[0])
"""output:[1 2]"""
print(arr[1])
"""output:[3 4]"""
print(arr[2])
"""output:[5 6]"""

# 2-D
array2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9], [10, 11, 12], [13, 14, 15], [16, 17, 18]])
array3 = np.array_split(array2, 6)
print(array3)
"""output:[array([[1, 2, 3]]), array([[4, 5, 6]]), array([[7, 8, 9]]), array([[10, 11, 12]]), array([[13, 14, 15]]), array([[16, 17, 18]])]"""

arr1 = np.array_split(array2, 3, axis=1)
print(arr1)
"""output:
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]"""

arr2 = np.hsplit(array2, 3)
print(arr2)
"""output:
[array([[ 1],
       [ 4],
       [ 7],
       [10],
       [13],
       [16]]), array([[ 2],
       [ 5],
       [ 8],
       [11],
       [14],
       [17]]), array([[ 3],
       [ 6],
       [ 9],
       [12],
       [15],
       [18]])]"""

arr3 = np.vsplit(array2, 2)
print(arr3)
"""outputs:
[array([[1, 2, 3],
       [4, 5, 6],
       [7, 8, 9]]), array([[10, 11, 12],
       [13, 14, 15],
       [16, 17, 18]])]
"""
# b6 = np.dsplit(array2)
# print(b6)
