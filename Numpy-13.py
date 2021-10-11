# Generate Random Number...
from numpy import array, random
from numpy.random.mtrand import rand, randint
Random = random.randint(100)
print(Random)
"""output: 33"""
# output can be anything because it's random




# Generate Random Float
Random2 = random.rand()
print(Random2)
"""output: 0.36435167584595163 
again it can be anything"""





# Generate Random Array
Random3 = random.randint(1, 100, size=(5))
print(Random3)
"""output:[66 56 11 92  6]"""

Random4 = random.randint(1000, size=(10))
print(Random4)
"""output: [257 597 944 861 982 203 960 432 220 553]"""
#Size is the number of random numbers





# Generate a 2-D array with 3 rows, each row containing 5 random integers from 0 to 100
Random5 = random.randint(100, size=(3, 5))
print(Random5) 
"""output:
[[20 56 50 75 97]
 [60 39 23 92 27]
 [41 22 45 58 82]]"""




# Floats 
Random6 = random.rand(5)
print(Random6)
"""output:[0.62998248 0.92165367 0.20609974 0.4959589  0.9047842 ]"""

Random7 = random.rand(3, 6)
print(Random7)
"""output:
[[0.59683386 0.62485423 0.99682284 0.91142369 0.12777953 0.3834824 ]
 [0.92278004 0.73310662 0.97689887 0.28304891 0.87013405 0.92272992]
 [0.04852857 0.67237412 0.86777089 0.46230992 0.92595637 0.38665551]]"""


# Generate Random Number From Array
Array1 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(Array1)
"""output:4
"""


Array2 = random.choice([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], size=(3, 5))
print(Array2)
"""output:
[[ 7  7  9  5  4]
 [ 2  2  5  8  5]
 [10  2  1  4 10]]
"""
