# Random Permutations of Elements
from numpy import random
import numpy as np

# Shuffling Arrays
array = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
random.shuffle(array)
print(array)
"""output:
[3 8 9 6 7 5 1 2 4]"""


# Generating Permutation of Arrays
array2 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
print(random.permutation(array2))
"""output:[7 8 9 4 1 6 5 3 2]"""

#Tip: the outputs can be anything because they are changing after each printing

"""The difference between shuffle() and permutation() is that shuffle() affects on all original but permutation() not"""
