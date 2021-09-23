# Dimensions in Arrays
# Keywords: .ndim , ndim='number of D'
"""examples of different dimensions in numpy """
"""we can find out the number of D by writting .ndim"""
import numpy as np

# D-0
arrayD_0 = np.array(10)
print(arrayD_0.ndim)
"""output:0"""

# D-1
arrayD_1 = np.array([1, 2, 3, 4, 5, 6])
print(arrayD_1.ndim)
"""output:1"""

# D-2
arrayD_2 = np.array([[1, 2, 3, 4, 5, 6, 7, 8]])
print(arrayD_2.ndim)
"""output:2"""

# D-3
arrayD_3 = np.array([[[1, 2, 3],[4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
print(arrayD_3.ndim)
"""output:3"""

"""Even we can give a dimension to an array"""
array_giving_D = np.array([1, 2, 3, 4], ndmin=4) #dimesion is 4
print(array_giving_D)
print(array_giving_D.ndim)
"""output:
[[[[1 2 3 4]]]]
4
."""
