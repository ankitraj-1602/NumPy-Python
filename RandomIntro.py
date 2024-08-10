# What is a Random Number?
# Random number does NOT mean a different number every time. Random means something that can not be predicted logically.

# Pseudo Random and True Random.
# Random numbers generated through a generation algorithm are called pseudo random.

# In order to generate a truly random number on our computers we need to get the random data from some outside source. This outside source is generally our keystrokes, mouse movements, data on network etc.
# We do not need truly random numbers, unless it is related to security

# Generate Random Number
from numpy import random

x = random.randint(100)
print(x)

# Generate Random Float

x = random.rand()
print(x)

# Generate Random Array
# The randint() method takes a size parameter where you can specify the shape of an array.

x= random.randint(100,size=(5))
y= random.rand(5,5)
print(x)
print(y)

# Generate Random Number From Array
# The choice() method allows you to generate a random value based on an array of values.
# The choice() method takes an array as a parameter and randomly returns one of the values.

x= random.choice([1,2,3,4,5])
print(x)

# The choice() method also allows you to return an array of values.

x= random.choice([1,2,3,4,5],size=2)
print(x)