# Searching Arrays
# You can search an array for a certain value, and return the indexes that get a match.
# To search an array, use the where() method.

import numpy as np

arr = np.array([1, 2, 3, 4, 5, 4, 4])
x = np.where(arr==4)
y = np.where(arr%2==0)
print(y)

# Search Sorted
# There is a method called searchsorted() which performs a binary search in the array, and returns the index where the specified value would be inserted to maintain the search order.

arr = np.array([6, 7, 8, 9])
x = np.searchsorted(arr,66)
print(x)

# By default the left most index is returned, but we can give side='right' to return the right most index instead.
x = np.searchsorted(arr, 7, side='right')
print(x)

# Multiple Values
# To search for more than one value, use an array with the specified values.

arr = np.array([1, 3, 5, 7])
x = np.searchsorted(arr,[2,4,10])
print(x)