# NumPy Array Indexing...
import  numpy as np
array = np.array([1, 'a', 2, 'b', 3])
print(array[0])
"""output:1"""

print(array[1])
"""output:a"""

print(array[2])
"""output:2"""

print(array[3])
"""output:b"""

print(array[4])
"""output:3"""

sum = array[0]+array[2]+array[4]
print(sum)
"""output:123"""


"""to get number from 2-D we should use comma (first number is number of demenision and the second number of value)"""
array_2D = np.array([[1, 2, 3],[4, 5, 6]])
"""now let's get 5"""
print(array_2D[1,1])
"""output:5"""


"""3"""
print(array_2D[0,2])
"""output:3"""


array_3D = np.array([[[1, 2, 3], [4, 5, 6]],[[7, 8, 9],[10, 11, 12]]])
"""4"""
print(array_3D[0,1,0])
"""output:4"""


"""6"""
print(array_3D[0,1,2])
"""output:6"""


"""9"""
print(array_3D[1,0,2])
"""output:9"""


"""12"""
print(array_3D[1,1,2])
# or
print(array_3D[1,1,-1])
"""output:12"""
