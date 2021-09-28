# Shape of an Array
import numpy as np 
array1 = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10],[11, 12, 13, 14, 15],[16, 17, 18, 19, 20]])
shape1 = array1.shape
print(shape1)
"""output:(4, 5)"""

array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], ndmin=3)
print(array2)
"""output:[[[ 1  2  3  4  5  6  7  8  9 10]]]"""

print(array2.shape)
"""output:(1, 1, 10)"""


# Array reshape
array3 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
print(array3.shape)
"""output:(20,)"""

array3reshape = array3.reshape(5, 4)
print(array3reshape)
"""output:
[[ 1  2  3  4]
 [ 5  6  7  8]
 [ 9 10 11 12]
 [13 14 15 16]
 [17 18 19 20]]
 """

array3reshape2 = array3.reshape(2, 2, 5)
print(array3reshape2)
"""output:
[[[ 1  2  3  4  5]
  [ 6  7  8  9 10]]
  """

