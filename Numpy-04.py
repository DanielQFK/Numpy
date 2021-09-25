# NumPy Array Slicing
import numpy as np

# 1-D
array1D = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
"""from 3 to 7"""
print(array1D[3:8])
"""output:[3 4 5 6 7]"""

"""all after 4"""
print(array1D[5:])
"""output:[ 5  6  7  8  9 10]"""

"""all before 5"""
print(array1D[:5])
"""output:[0 1 2 3 4]"""

"""number 8 and 9"""
print(array1D[-3:-1])
"""output:[8 9]"""

"""only even numbers"""
print(array1D[:-1:2])
"""output:[0 2 4 6 8]"""

"""reversed number"""
print(array1D[::-1])
"""output[10  9  8  7  6  5  4  3  2  1  0]"""


# Slicing 2-D Arrays.
array2D = np.array([[1, 2, 3, 4, 5],[6, 7, 8, 9, 10]])
"""after 3"""
print(array2D[0, 2:5])
"""output:[3 4 5]"""

"""6 to 9"""
print(array2D[1, 0:4])
"""output:[6 7 8 9]"""

"""both arrays three between numbers"""
print(array2D[0:2, 1:4])
"""output:
[[2 3 4]
 [7 8 9]]"""

"""all numbers"""
print(array2D[0:2, 0:5])
"""output:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]"""
