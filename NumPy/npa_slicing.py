#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].

import numpy as np
# Slicing 1-D Arrays
#Slice elements from index 1 to 5 
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Slice elements from index 4 to the end of the array
print(arr[4:])

#Slice elements from the beginning to index 4 (not included):
print(arr[:4])

#Use the step value to determine the step of the slicing:
#Return every other element from index 1 to index 5:
print(arr[1:5:2])

#Return every other element from the entire array:
print(arr[::2])

#Slicing 2-D Arrays

arr = np.array([[1, 2, 3, 4, 5], [6, 7, 8, 9, 10]])

#From the second element, slice elements from index 1 to index 4 (not included):
print(arr[1, 1:4]) # -> 0 for 1st arr and 1 for 2nd arr
