# Copy and View
import numpy as np

# Copy
# Copy is the original array
array1 = np.array([1, 2, 3, 4, 5, 6])
copy_array = array1.copy()
copy_array[0] = 7
print(copy_array) # now you can the place 0 has been changed
"""output:[7 2 3 4 5 6]"""

print(array1) # now you can see the original one and the original one hasn't changed . that's what copy() does
"""output:[1 2 3 4 5 6]"""

# View
array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
view_array2 = array2.view()
view_array2[0] = 10
print(view_array2) # now you can see it has changed but
"""output:[10  2  3  4  5  6  7  8  9 10]"""

print(array2) # not only that but both the original one also has changed . it means it has affected on the original one too...
"""output:[10  2  3  4  5  6  7  8  9 10]"""


# base
print(copy_array.base) # it shows 'None' because copy variables doesn't have a base 
"""output:None"""

print(view_array2.base) # but view variables has because they some kind represent the main varable
"""output:[10  2  3  4  5  6  7  8  9 10]"""

