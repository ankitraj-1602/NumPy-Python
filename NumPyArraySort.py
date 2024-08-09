# Sorting Arrays
# Sorting means putting elements in an ordered sequence.
# Ordered sequence is any sequence that has an order corresponding to elements, like numeric or alphabetical, ascending or descending.
# The NumPy ndarray object has a function called sort(), that will sort a specified array.

import numpy as np

arr = np.array([3, 2, 0, 1])
print(np.sort(arr))

# Sorting a 2-D Array
# If you use the sort() method on a 2-D array, both arrays will be sorted:

arr = np.array([[3, 2, 4], [5, 0, 1]])
print(np.sort(arr))

# Filtering Arrays
# Getting some elements out of an existing array and creating a new array out of them is called filtering.

arr = np.array([41, 42, 43, 44])
filterparams = [True,False,True,True]
newarr = arr[filterparams]
print(newarr)

# Creating the Filter Array
# In the example above we hard-coded the True and False values, but the common use is to create a filter array based on conditions.

arr = np.array([41, 42, 43, 44])

# Create an empty list
filter_arr = []

# go through each element in arr
for element in arr:
  # if the element is higher than 42, set the value to True, otherwise False:
  if element > 42:
    filter_arr.append(True)
  else:
    filter_arr.append(False)

newarr = arr[filter_arr]

print(filter_arr)
print(newarr)

# Creating Filter Directly From Array
# The above example is quite a common task in NumPy and NumPy provides a nice way to tackle it.
# We can directly substitute the array instead of the iterable variable in our condition and it will work just as we expect it to.

arr = np.array([41, 42, 43, 44])
filter_arr = arr > 43
newarr = arr[filter_arr]
print(newarr)