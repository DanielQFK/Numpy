# Getting start and making array
# Keywords:np, .array , type
"""to use numpy library, at first you should install numpy on your system then import it..."""
import numpy as np
"""We can create a NumPy ndarray object by using the array() function."""
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(array1)
"""output:[ 1  2  3  4  5  6  7  8  9 10]"""

# e.g. 2
array2 = np.array([1 , 2 , 3 , 4 , 5 , 6])
print(array2)
print(type(array2)) # to tell us the type of this value
"""output:
[1 2 3 4 5 6]
<class 'numpy.ndarray'>"""

# e.g. 3
"""tuple or any array-like object into the array() method"""
array3 = np.array((1 , 2 , 3 , 4 , 5 , 6))
print(array3)
print(type(array3))
"""output:
[1 2 3 4 5 6]
<<<<<<< HEAD
<class 'numpy.ndarray'>"""
=======
<class 'numpy.ndarray'>"""
>>>>>>> d50faab3a8cacea6b282d83e5b8083c1e118cb46
