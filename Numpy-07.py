# Iterating Arrays
import numpy as np
array1 = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
for x in array1:
    print(x)
"""output:
1
2
3
4
5
6
7
8
9
10"""

array2 = np.array([[1, 2, 3], [4, 5, 6]])
for y in array2:
  print(y) # it prints each array
"""ourpur:
[1 2 3]
[4 5 6]"""  
for y in array2:
    for z in y:
        print(z) # ir prints each number    
"""output:
1
2
3
4
5
6"""

array3 = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])
for q in array3:
    print(q)
"""output:
[[1 2 3]
 [4 5 6]]
[[ 7  8  9]
 [10 11 12]]
"""

for q in array3:    
    for w in q:
        print(w)
"""output:
[1 2 3]
[4 5 6]
[7 8 9]
[10 11 12]
"""

for q in array3:    
    for w in q:        
        for e in w:
            print(e) # it prints all numbers
"""output:
1
2
3
4
5
6
7
8
9
10
11
12"""


# Iterating Arrays Using nditer()
array4 =  np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
for t in np.nditer(array4):
    print(t)
"""output:
1
2
3
4
5
6
7
8"""

#* Iterating Array With Different Data Types
array5 = np.array([1, 2, 3])
for p in np.nditer(array5, flags=['buffered'], op_dtypes='S'):
    print(p)
"""output:
b'1'
b'2'
b'3'"""


# Iterating With Different Step Size
array6 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for x1 in np.nditer(array6[: , ::2]):
  print(x1)
"""output:
1
3
5
7"""

#  Enumerated Iteration Using ndenumerate()
array7 = np.array([1, 2, 3])
for xx, yy in np.ndenumerate(array7):
  print(xx , yy)
"""output:
(0,) 1
(1,) 2
(2,) 3"""

array8 = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
for qq, ww in np.ndenumerate(array8):
  print(qq, ww)  
"""output:
(0, 0) 1
(0, 1) 2
(0, 2) 3
(0, 3) 4
(1, 0) 5
(1, 1) 6
(1, 2) 7
(1, 3) 8"""
