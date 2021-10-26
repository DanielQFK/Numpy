# Add the Elements of Two Lists
import numpy as np
one = np.array([1, 2, 3, 4, 5])
two = np.array([6, 7, 8, 9, 10])
three = []
for i, j in zip(one, two):
    three.append(i + j)
print(three)
"""output:
[7, 9, 11, 13, 15]"""  

four = np.add(one, two)
print(four)
"""output:
[ 7  9 11 13 15]"""