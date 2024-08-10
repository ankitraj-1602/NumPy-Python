# How To Create Your Own ufunc
# To create your own ufunc, you have to define a function, like you do with normal functions in Python, then you add it to your NumPy ufunc library with the frompyfunc() method.

# The frompyfunc() method takes the following arguments:

# function - the name of the function.
# inputs - the number of input arguments (arrays).
# outputs - the number of output arrays.

import numpy as np

def myadd(x,y):
    return x+y

myadd = np.frompyfunc(myadd,2,1)
print(myadd([1,2],[1,2]))

# Check if a Function is a ufunc
# Check the type of a function to check if it is a ufunc or not.

# A ufunc should return <class 'numpy.ufunc'>.

import numpy as np

print(type(np.add))