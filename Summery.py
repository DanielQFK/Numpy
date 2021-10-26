import numpy as np
import pytube

#making an array
array1 = np.array([1, 2, 3, 4])
print(array1)
"""output:
[1 2 3 4]
"""
# 2-D array
array2 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
print(array2)
"""output:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]
 """

# Get dimension
Dimension1 = array1.ndim
print(Dimension1)
"""output: 1"""
Dimension2 = array2.ndim
print(Dimension2)
"""output: 2"""


# Get shape
# (Rows, Column)
shape1 = array1.shape
print(shape1)
"""output:(4,)"""
shape2 = array2.shape
print(shape2)
"""output:(2, 5)"""

# Get bytes
print(array1.dtype)
"""output: int64"""
array3 = np.array([1, 2, 3, 4, 5], dtype='int16')
print(array3.dtype)
"""output:int16"""
print(array3.itemsize)
"""output: 2"""


# Get specific item
Name = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
# I wanna get 10 [row,column]
print(Name[1,4]) #or
print(Name[1,-1])
"""output:
10 
10"""

#Get specific row
print(Name[0,:])
"""output:[1 2 3 4 5]"""
# Get specific column
print(Name[:,2])
"""output;[3 8]"""

# all 0s and 1s matrix
zeros = np.zeros([1, 2, 3])
ones = np.ones([2, 3, 4])
print(zeros , "\n" , ones)
"""output:
[[[0. 0. 0.]
  [0. 0. 0.]]]
..................... 
 [[[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]

 [[1. 1. 1. 1.]
  [1. 1. 1. 1.]
  [1. 1. 1. 1.]]]"""

# Full number
full1 = np.full([1, 2], 123)
print(full1)
"""output = [[123 123]]"""

# similar shape but other numbers
full_like = np.full_like([full1], 0) #or np.full(full1.shape)
print(full_like)
"""output = [[0 0]]"""

