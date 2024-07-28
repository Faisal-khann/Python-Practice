'''
Logistic Distribution is used to describe growth.
Used extensively in machine learning in logistic regression, neural networks etc.
It has three parameters:
1-> loc - mean, where the peak is. Default 0.
2-> scale - standard deviation, the flatness of distribution. Default 1.
3-> size - The shape of the returned array.
'''

from numpy import random as r
import matplotlib.pyplot as plt
import seaborn as sns

# Q. Draw 2x3 samples from a logistic distribution with mean at 1 and stddev 2.0:
x = r.logistic(loc=1, scale=2, size=(2, 3))
print(x)

#Visualization
sns.distplot(r.logistic(size=1000), hist=False)
plt.show()