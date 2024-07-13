'''Data Distribution is a list of all possible
   values, and how often each value occurs.

   Random Distribution -> A random distribution is a set of random numbers that follow a certain probability density function.
   We can generate random numbers based on defined probabilities using the choice() method of the random module.

Q. Generate a 1-D array containing 10 values, where each value has to be 3, 5, 7 or 9
  and its probabilities is 0.1, 0.3, 0.6, 0.0
'''

from numpy import random
x = random.choice([3, 5, 6, 9], p = [0.1, 0.3, 0.6, 0.0], size=(10))
print(x)