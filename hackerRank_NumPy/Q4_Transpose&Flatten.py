import numpy as np
# Firstly need to change given list into numpy array
# n, m = map(int, input().split())
nm = input().split
n, m = int(nm[0]), int(nm[1])
l = [input().split() for i in range(n)]
arr = np.array(l, dtype= int)
print(np.transpose(arr))
print(arr.flatten())