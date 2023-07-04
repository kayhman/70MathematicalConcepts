import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Least Squares method to calculate parameters.
def fit(X, Y):
    return inv(X.T.dot(X)).dot(X.T).dot(Y)

# The relation we are looking for here is of the type $ y = a * x $, with $a \approx 1.0$.
X = np.array([[3.1], [1.01], [1.98], [2.02], [2.93], [3.07]])
Y = np.array([2.9, 0.9, 2.3, 2.05, 2.8, 3.12])

linear_params = fit(X, Y)
print(linear_params)
# > [0.99278671]

# The relation we are looking for here is of the type $ y = a * x + b $, with $a \approx 1.0$ and $b \approx 0.0$.
X = np.array([[1, 3.1], [1, 1.01], [1, 1.98], [1, 2.02], [1, 2.93], [1, 3.07]])
affine_params = fit(X, Y)
print(affine_params)
# > [0.10908029
#    0.95078088]

# Plotting the curve.
plt.scatter([x[1] for x in X], Y)
plt.plot(np.linspace(1, 3, 10),
         np.linspace(1, 3, 10) * linear_params[0],
         ':', label='linear')
plt.plot(np.linspace(1, 3, 10),
         np.linspace(1, 3, 10) * affine_params[1] + affine_params[0],
         '-.', label='affine')
plt.legend()
plt.show()
