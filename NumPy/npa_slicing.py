#Slicing in python means taking elements from one given index to another given index.
#We pass slice instead of index like this: [start:end].
#We can also define the step, like this: [start:end:step].

import numpy as np
#Slice elements from index 1 to 5 
arr = np.array([1, 2, 3, 4, 5, 6, 7])
print(arr[1:5])

#Slice elements from index 4 to the end of the array
print(arr[4:])

#Slice elements from the beginning to index 4 (not included):
print(arr[:4])