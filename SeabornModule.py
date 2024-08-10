# Visualize Distributions With Seaborn
# Seaborn is a library that uses Matplotlib underneath to plot graphs. It will be used to visualize random distributions.

# Distplots
# Distplot stands for distribution plot, it takes as input an array and plots a curve corresponding to the distribution of points in the array.

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([1,2,3,4,5,6,7])
plt.show()

import matplotlib.pyplot as plt
import seaborn as sns

sns.distplot([0, 1, 2, 3, 4, 5], hist=False)

plt.show()