# Use the random.normal() method to get a Normal Data Distribution.
# It has three parameters:
# loc - (Mean) where the peak of the bell exists.
# scale - (Standard Deviation) how flat the graph distribution should be.
# size - The shape of the returned array.

# Generate a random normal distribution of size 2*3
from numpy import random
x = random.normal(size=(2, 3))
print(x)
print()

# Generate a random normal distribution of size 2x3 with mean at 1 and standard deviation of 2:
x = random.normal(loc=1, scale=2, size=(2, 3))
print(x)
print()

# Visualization of Normal Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(size=100), hist = False)
plt.show()