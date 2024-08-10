# What is Data Distribution?
# Data Distribution is a list of all possible values, and how often each value occurs.
# Such lists are important when working with statistics and data science.
# The random module offer methods that returns randomly generated data distributions.

# Random Distribution
# A random distribution is a set of random numbers that follow a certain probability density function.
# Probability Density Function: A function that describes a continuous probability. i.e. probability of all values in an array.
# We can generate random numbers based on defined probabilities using the choice() method of the random module.
# The choice() method allows us to specify the probability for each value.

from numpy import random

x= random.choice([1,2,3,4,5],p=[0.1,0.2,0.3,0.4,0],size=20)
print(x)