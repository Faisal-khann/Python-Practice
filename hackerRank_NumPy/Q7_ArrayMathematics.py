"""
***Task***
You are given two integer arrays, and of dimensions X.
Your task is to perform the following operations:

Add ( + )
Subtract ( - )
Multiply ( * )
Integer Division ( / )
Mod ( % )
Power ( ** )

Note
There is a method numpy.floor_divide() that works like numpy.divide() except it performs a floor division.

***Input Format***
The first line contains two space separated integers,  and .
The next  lines contains  space separated integers of array .
The following  lines contains  space separated integers of array .

***Output Format***
Print the result of each operation in the given order under Task.

***Sample Input***
1 4
1 2 3 4
5 6 7 8

***Sample Output***
[[ 6  8 10 12]]
[[-4 -4 -4 -4]]
[[ 5 12 21 32]]
[[0 0 0 0]]
[[1 2 3 4]]
[[    1    64  2187 65536]] 

Use // for division in Python 3.
"""

import numpy as np

# Read input dimensions
n, m = map(int, input().split())

# Read array a
a = np.array([input().split() for _ in range(n)], dtype=int)

# Read array b
b = np.array([input().split() for _ in range(n)], dtype=int)

# Perform operations and print results
print(np.add(a, b))
print(np.subtract(a, b))
print(np.multiply(a, b))
print(np.floor_divide(a, b))  # Integer division
print(np.mod(a, b))
print(np.power(a, b))

