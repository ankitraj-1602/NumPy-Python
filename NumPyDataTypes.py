# Data Types in NumPy
# NumPy has some extra data types, and refer to data types with one character, like i for integers, u for unsigned integers etc.
# Below is a list of all data types in NumPy and the characters used to represent them.
# i - integer
# b - boolean
# u - unsigned integer
# f - float
# c - complex float
# m - timedelta
# M - datetime
# O - object
# S - string
# U - unicode string
# V - fixed chunk of memory for other type ( void )

# Checking the Data Type of an Array
# The NumPy array object has a property called dtype that returns the data type of the array:

import numpy as np

arr = np.array([1, 2, 3, 4])
arr2 = np.array(['apple', 'banana', 'cherry'])
print(arr.dtype)
print(arr2.dtype)

# Creating Arrays With a Defined Data Type
# We use the array() function to create arrays, this function can take an optional argument: dtype that allows us to define the expected data type of the array elements:

arr = np.array([1, 2, 3, 4], dtype='S')
print(arr)
print(arr.dtype)

# What if a Value Can Not Be Converted?
# If a type is given in which elements can't be casted then NumPy will raise a ValueError.
# ValueError: In Python ValueError is raised when the type of passed argument to a function is unexpected/incorrect.

# Converting Data Type on Existing Arrays
# The best way to change the data type of an existing array, is to make a copy of the array with the astype() method.
# The astype() function creates a copy of the array, and allows you to specify the data type as a parameter.
# The data type can be specified using a string, like 'f' for float, 'i' for integer etc. or you can use the data type directly like float for float and int for integer.

arr = np.array([1.1, 2.1, 3.1])
newarr = arr.astype('i')
print(newarr)