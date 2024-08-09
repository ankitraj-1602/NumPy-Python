# Shape of an Array
# The shape of an array is the number of elements in each dimension.

# Get the Shape of an Array
# NumPy arrays have an attribute called shape that returns a tuple with each index having the number of corresponding elements.

import numpy as np

arr = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])
print(arr.shape)

arr =np.array([1,2,3],ndmin=5)
print(arr)
print(arr.shape)


# Reshaping arrays
# Reshaping means changing the shape of an array.
# The shape of an array is the number of elements in each dimension.
# By reshaping we can add or remove dimensions or change number of elements in each dimension.

# Reshape From 1-D to 2-D

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12])
x= arr.reshape(4,3)
print(x)

# Reshape From 1-D to 3-D

newarr= arr.reshape(2,3,2)
print(newarr)
print(newarr.shape)

# Returns Copy or View?
# The example above returns the original array, so it is a view.

# Unknown Dimension
# You are allowed to have one "unknown" dimension.
# Meaning that you do not have to specify an exact number for one of the dimensions in the reshape method.
# Pass -1 as the value, and NumPy will calculate this number for you.

arr = np.array([1, 2, 3, 4, 5, 6, 7, 8])

newarr = arr.reshape(2, 2, -1)

print(newarr)

# Flattening the arrays
# Flattening array means converting a multidimensional array into a 1D array.
# We can use reshape(-1) to do this.

arr = np.array([[1, 2, 3], [4, 5, 6]])
newarr = arr.reshape(-1)
print(newarr)