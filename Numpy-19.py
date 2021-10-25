# vertically stack vectors
import numpy as np
array = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
print(np.vstack([array, array2, array2, array]))
"""Output:"""


# Horizontal stack vectors 
print(np.hstack([array, array2]))

