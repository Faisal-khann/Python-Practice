'''
Poisson Distribution is a Discrete Distribution.
It estimates how many times an event can happen in a specified time. e.g. If someone eats twice a day what is the probability he will eat thrice?

It has two parameters:
1-> lam - rate or known number of occurrences e.g. 2 for above problem.
2-> size - The shape of the returned array.
'''
# from numpy import random as r

# Generate a random 1x10 distribution for occurrence 2:
# x = r.poisson(lam=2, size=10)
# print('\n possion: \n', x)

# Visualization of Poisson Distribution
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(r.poisson(lam=2, size=1000), kde=False)
plt.show()

'''
1. Normal continous kai liye hota hai and isme +ve and -ve
dono value hoti hai
2. Possion non-negative value hoti hai and isliye they called it discrete 

'''

from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot(random.normal(loc=50, scale=7, size=1000), hist=False, label="normal")
sns.distplot(random.poisson(lam=50, size=1000), hist=False, label="poisson")

plt.show()