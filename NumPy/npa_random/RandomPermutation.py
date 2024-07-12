# permutation refers to an arrangement of elements. e.g. [3, 2, 1] is a permutation of [1, 2, 3] and vice-versa.
# The NumPy Random module provides two methods for this: shuffle() and permutation().

# Shuffling Arrays -> Shuffle means changing arrangement of elements in-place. i.e. in the array itself.
from numpy import random
import numpy as np
arr = np.array([1, 2, 3, 4, 5])
random.shuffle(arr)
print("After Shuffling: ", arr)
#The shuffle() method makes changes to the original array.

# Generating Permutation of Arrays
print("After generating random permutation: ",random.permutation(arr))


