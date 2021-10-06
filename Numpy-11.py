# Sorting Arrays...
import numpy as np
from numpy.core.fromnumeric import sort
array1 = np.array([1, 6, 2, 4, 3, 5, 0])
print(np.sort(array1))
"""output
[0 1 2 3 4 5 6]"""

array2 = np.array(['E', 'D', 'B', 'C', 'A'])
print(np.sort(array2))
"""output
['A' 'B' 'C' 'D' 'E']"""

array3 = np.array([True, False, True, False])
print(np.sort(array3))
"""output
[False False  True  True]"""

array4 = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(array4))
"""output
[[2 3 4]
 [0 1 5]]"""
 
