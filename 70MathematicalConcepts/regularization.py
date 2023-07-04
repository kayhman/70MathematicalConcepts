import numpy as np
import matplotlib.pyplot as plt
plt.style.use('grayscale')

x = np.linspace(-20, 20, 200)
# Absolute value of x is calculated
y = np.abs(x)
# An approximation of the absolute value of x is calculated here
# with the log(cosh)
y_logcosh = np.log(np.cosh(x))
plt.plot(x, y, label=f'Absolute error')
plt.plot(x, y_logcosh, label=f'log(cosh)')
plt.legend(loc='upper left')
plt.show()

# At zero, the two functions
# both have a value of 0
print(np.abs(0.0))
#> 0.0
print(np.log(np.cosh(0)))
#> 0.0

# For a sufficiently positive value
# the difference between the two is indeed log(2)
print(np.log(np.cosh(10)) - 10 + np.log(2))
#> 2.0611529150116326e-09

# The same is true
# for a sufficiently negative value
print(np.log(np.cosh(-10)) - 10 + np.log(2))
#> 2.0611529150116326e-09
