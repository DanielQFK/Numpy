# statistic...
import numpy as np
array = np.array([[1, 2, 3],[4, 5, 6]])
print(array)
"""output:
[[1 2 3]
 [4 5 6]]"""

print(np.min(array))
"""output:1"""


print(np.max(array))
"""output:6"""

print(np.min(array, axis=0))
"""output:123"""

print(np.max(array, axis=1))
"""output:36"""

print(np.sum(array))
"""output:21"""

# reshaping
print(array.shape)
"""output:(2, 3)"""
print(array.reshape((6, 1)))
"""output:
[[1]
 [2]
 [3]
 [4]
 [5]
 [6]]"""
