'''
***Task***
You are given the shape of the array in the form of space-separated integers,
each integer representing the size of different dimensions, your task is to print 
an array of the given shape and integer type using the tools numpy.zeros and numpy.ones.

***Input Format***
A single line containing the space-separated integers.


***Output Format***
First, print the array using the numpy.zeros tool and 
then print the array with the numpy.ones tool.

Sample Input 0

3 3 3
Sample Output 0

[[[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]

 [[0 0 0]
  [0 0 0]
  [0 0 0]]]
[[[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]

 [[1 1 1]
  [1 1 1]
  [1 1 1]]]
'''

import numpy as np

# Read the input
shape = tuple(map(int, input().split()))

# Create an array with zeros
zeros_array = np.zeros(shape, dtype=int)

# Create an array with ones
ones_array = np.ones(shape, dtype=int)

# Print the arrays
print(zeros_array)
print(ones_array)
