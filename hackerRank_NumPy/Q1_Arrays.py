import numpy

def arrays(arr):
    num_array = numpy.array(arr, float)
    return num_array[::-1]

arr = input().strip().split(' ')
result = arrays(arr)
print(result)

'''
***Output Format***
Print the reverse NumPy array with type float.

Sample Input
1 2 3 4 -8 -10

Sample Output
[-10.  -8.   4.   3.   2.   1.]

'''