# Shuffling Arrays
# Shuffle means changing arrangement of elements in-place. i.e. in the array itself.

from numpy import random
import numpy as np

arr = np.array([1,2,3,4,5,6,7,8])
x= random.shuffle(arr)
print(x) #inplace permutation
print(arr)

# Generating Permutation of Arrays

x= random.permutation(arr)
print(x)