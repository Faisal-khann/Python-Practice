'''
Uniform Distribution
Used to describe probability where every event has equal chances of occuring.
E.g. Generation of random numbers.

It has three parameters:
1-> a - lower bound - default 0 .0.
2-> b - upper bound - default 1.0.
3-> size - The shape of the returned array.
'''

#Create a 2x3 uniform distribution sample:
# from numpy import random
# x = random.uniform(size=(2, 3))
# x = random.uniform(0.2, 0.4, size=(10))
# print(x) 

# Visualization of Uniform Distribution
from numpy import random
import matplotlib.pyplot as plt
import seaborn as sns

# x = random.uniform(size=(1000))
sns.distplot(random.uniform(size=1000), hist=False, label="Uniform")
plt.show()
print(x)