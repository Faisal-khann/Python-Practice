'''
Task-> You are given a space separated list of nine integers. 
       Your task is to convert this list into a X NumPy array.

Input Format-> A single line of input containing  space separated integers.
Output Format-? Print the 3*3 NumPy array.

Sample Input 
1 2 3 4 5 6 7 8 9

Sample Output
[[1 2 3]
 [4 5 6]
 [7 8 9]]
 
'''

import numpy as np
# l = list(map(int, input().split())) # change list convert into array
l = input().split()
arr = np.array(l, dtype=int)
print(arr.reshape(3, 3))

'''
Method 2->
print(np.array(input().split(), dtype=int).reshape(3, 3))

'''
