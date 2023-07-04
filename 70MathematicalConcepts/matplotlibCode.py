# Installation is done with pip: pip install matplotlib
# The library is imported as follows
import matplotlib.pyplot as plt
import random

# Plotting a scatter plot is done as follows
X = [random.random() - 0.5 for i in range(0, 100)]
Y = [random.random() - 0.5 for i in range(0, 100)]
plt.scatter(X, Y)
plt.show()

# Plotting a curve is done as follows
X = [i for i in range(-50, 50)]
Y = [x**2 for x in X]
plt.plot(X, Y)
plt.show()