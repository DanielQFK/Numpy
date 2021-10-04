# Searching Arrays
import numpy as np
from numpy.core.fromnumeric import searchsorted
array1 = np.array([0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
search1 = np.where(array1==16)
print(search1) # it shows the place of nuber 2 in array a
"""output:(array([15]),)"""

#even numbers
search2 = np.where(array1%2==0)
print(search2)
"""output:(array([ 0,  2,  4,  6,  8, 10, 12, 14, 16, 18, 20, 22, 24, 26, 28, 30]),)"""

#odd numbers
print(np.where(array1%2!=0))
"""output:(array([ 1,  3,  5,  7,  9, 11, 13, 15, 17, 19, 21, 23, 25, 27, 29]),)"""

# Search Sorted
array2 = np.array([222, 333, 444, 555, 666, 777, 888, 999])
search3 = np.searchsorted(array2, 333)
print(search3) # just says the number of the place
"""output:1"""


# Search From the Right Side
search4 = np.searchsorted(array2, 555, side='right')
print(search4) # just says the number of the place
"""output:4"""

# Multiple Values
array3 = np.array([1, 3, 5, 7, 9])
search5 = np.searchsorted(array3, [2, 4, 6, 8])
print(search5)
"""output:[1 2 3 4]"""
