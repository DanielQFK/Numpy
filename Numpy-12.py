# Filtering Arrays...
import numpy as np
array1 = np.array([41, 42, 43, 44, 45, 46, 47])
array2 = [True, False, True, False, False, False, True]
array3 = array1[array2]
print(array3)
"""output:[41 43 47]"""

# Creating the Filter Array
Filtering = np.array([41, 42, 43, 44])
Filtering1 = []
for element in Filtering:
    if element > 42:
        Filtering1.append(True)
    else:
        Filtering1.append(False)
Filtering2 = Filtering[Filtering1]
print(Filtering)
print(Filtering1)
print(Filtering2)
"""output:
[41 42 43 44]
[False, False, True, True]
[43 44]"""

# Creating Filter Directly From Array
array4 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
Filter_N1 = array4<8
New_N1 = array4[Filter_N1]
print(New_N1)
"""output:[1 2 3 4 5 6 7]"""


