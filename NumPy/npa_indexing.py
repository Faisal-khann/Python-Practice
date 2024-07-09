# The indexes in NumPy arrays start with 0,
#meaning that the first element has index 0, and the second has index 1 etc.
import numpy as np
arr = np.array([1, 2, 3, 4])

print("Element of 0th index : ",arr[0])
print("Element of 3rd index : ",arr[3])
print(arr[2]+arr[3]) #get third and fourth elements from the following array and add them.

print()
# Access 2-D Arrays
# To access elements from 2-D arrays we can use comma separated integers representing the dimension and the index of the element.

#Think of 2-D arrays like a table with rows and columns, where the dimension represents the row and the index represents the column.
arr = np.array([[1,2,3,4,5], [6,7,8,9,10]])

print('2nd element on 1st row: ', arr[0, 1])

print()

#Access 3-D Arrays
arr = np.array([[[1, 2, 3], [4, 5, 6]], [[7, 8, 9], [10, 11, 12]]])

print(arr[0, 1, 2])

