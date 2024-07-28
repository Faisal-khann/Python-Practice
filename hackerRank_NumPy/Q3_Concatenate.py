# import numpy
# n, m, p = [int(i) for i in input().split()]

# arr1 = numpy.array([input().split() for i in range(n)], int)
# arr2 = numpy.array([input().split() for j in range(m)], int)
# print(numpy.concatenate((arr1, arr2), axis = 0))

import numpy as np
array_1 = np.array([1,2,3])
array_2 = np.array([4,5,6])
array_3 = np.array([7,8,9])

print (np.concatenate((array_1, array_2, array_3)))  