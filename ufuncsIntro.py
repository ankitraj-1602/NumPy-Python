# What are ufuncs?
# ufuncs stands for "Universal Functions" and they are NumPy functions that operate on the ndarray object.

# Why use ufuncs?
# ufuncs are used to implement vectorization in NumPy which is way faster than iterating over elements.

# They also provide broadcasting and additional methods like reduce, accumulate etc. that are very helpful for computation.

# What is Vectorization?
# Converting iterative statements into a vector based operation is called vectorization.

# It is faster as modern CPUs are optimized for such operations.

import numpy as np

x=[1,2,3,4]
y=[2,3,4,5]

print(np.add(x,y))