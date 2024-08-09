# Create a NumPy ndarray Object
# NumPy is used to work with arrays. The array object in NumPy is called ndarray.
# We can create a NumPy ndarray object by using the array() function.

import numpy as np
arr = np.array([1,2,3])
print(arr)
print(type(arr))

# To create an ndarray, we can pass a list, tuple or any array-like object into the array() method, and it will be converted into an ndarray:

arr = np.array((1,2,3))
print(arr)

# 0-D Arrays
# 0-D arrays, or Scalars, are the elements in an array. Each value in an array is a 0-D array.

arr = np.array(42)
print(arr)

# 1-D Arrays
# An array that has 0-D arrays as its elements is called uni-dimensional or 1-D array.

arr = np.array([1,2,3,4])
print(arr)

# 2-D Arrays
# An array that has 1-D arrays as its elements is called a 2-D array.

arr = np.array([[1, 2, 3], [4, 5, 6]])
print(arr.ndim)

# 3-D arrays
# An array that has 2-D arrays (matrices) as its elements is called 3-D array.

arr = np.array([[[1, 2, 3], [4, 5, 6]], [[1, 2, 3], [4, 5, 6]]])
print(arr.ndim)

# Higher Dimensional Arrays
# An array can have any number of dimensions.
# When the array is created, you can define the number of dimensions by using the ndmin argument.

arr = np.array([1,2,3,4,5],ndmin=6)
print(arr)
print(arr.ndim)