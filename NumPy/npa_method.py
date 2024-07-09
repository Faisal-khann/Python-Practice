import numpy as np

# Join Np Array
arr1 = np.array([1, 2, 3])
arr2 = np.array([4, 5, 6])
arr = np.concatenate((arr1, arr2))
print("After joining:", arr)

print()

# Joining Arrays Using Stack Functions
# We pass a sequence of arrays that we want to join to the stack() method along with the axis
arr = np.stack((arr1, arr2), axis=1)
print("After Joining:", arr)

print()

# Spliting Arrays -> Splitting is reverse operation of Joining.
# We use array_split() for splitting arrays, we pass it the array we want to split and the number of splits.
arr = np.array([1, 2, 3, 4, 5, 6])

newarr = np.array_split(arr, 3)

print("After spliting: ", newarr)

print()

# Searching Arrays -> To search an array, use the where() method.
# Q.Find the indexes where the value is 4:
arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr == 4)
print(x)

# Q. Find the indexes where the values are even:
arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

x = np.where(arr%2 == 0)

print(x)

# Sorting Np Array
arr = np.array([10, 30, 5, 20])
print("After Sorting:", np.sort(arr))

#
