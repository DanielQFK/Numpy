from numpy import random
from numpy.random.mtrand import rand

# Random Distribution(probability)...
Random_probablity = random.choice([1, 56, 23, 75], p=[0.2, 0.4, 0.2, 0.2], size=(100)) #The sum of all of probablities should be 1
print(Random_probablity)
"""output:
[56 56 56 56 56 56 56 23  1 75 56 56  1 56 56 56 56 56 56 23  1 23  1 23
 75 56 23 56 56 56  1 56 23 75 23 56 56 56  1 56 23 75 23 56 56 75 75 56
 56  1 56 75 75 56 56 56  1 56 56 23 56 56 56 56  1  1 23 23  1 56 56 23
 56 56 56 56 23  1 56  1 56 56  1 56  1  1 23 23 56  1 23 56 75 23  1 56
 75  1 23 56]"""

Random_probablity2 = random.choice([1, 11, 111], p=[0.8, 0.1, 0.1], size=(4, 10))
print(Random_probablity2)
"""output:
[[  1   1   1   1   1  11   1   1 111   1]
 [ 11 111   1   1   1   1   1   1 111   1]
 [ 11   1   1   1   1 111 111 111   1   1]
 [  1   1   1   1   1  11   1   1   1   1]]"""
