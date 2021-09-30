# Joining NumPy Arrays...
import numpy as np
array1 = np.array([1, 2, 3, 4, 5])
array2 = np.array([6, 7, 8, 9, 10])
mix1 = np.concatenate(array1, array2)
print(mix1) ## values of both variables are together
"""outputs:
[ 1  2  3  4  5  6  7  8  9 10]
"""

# Joining Arrays Using Stack Functions
mix2 = np.stack(array1, array2)
print(mix2)
"""outputs:
[[ 1  6]
 [ 2  7]
 [ 3  8]
 [ 4  9]
 [ 5 10]]
 """

# Stacking Along Rows
mix3 = np.hstack(array1, array2)
print(mix3)
"""outputs:
[ 1  2  3  4  5  6  7  8  9 10]
"""

# Stacking Along Columns
mix4 = np.vstack(array1, array2)
print(mix4)
"""outputs:
[[ 1  2  3  4  5]
 [ 6  7  8  9 10]]"""

# Stacking Along Height (depth)
mix5 = np.dstack(array1, array2)
print(mix5) #similar to Stack(())
"""outputs:
[[[ 1  6]
  [ 2  7]
  [ 3  8]
  [ 4  9]
  [ 5 10]]]"""
