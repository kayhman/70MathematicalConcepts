import numpy as np
from numpy.linalg import inv
import matplotlib.pyplot as plt

# Calculation of parameters using least squares method.
def fit(X, Y):
    return inv(X.T.dot(X)).dot(X.T).dot(Y)

# The radius of the wind turbine blades is 50\:m.
R = 50
# The resulting area is $S = S \pi r^2$.
S = 2 * 3.1415 * R**2

# The wind speed is taken between 0 and 30 $\frac{m}{s}$.
V = np.linspace(0, 30, 50)
V_3 = 8.0 / 27.0 * S * np.array([[v**3] for v in V])
# Air density
rho = 1.292
# Calculation of power according to the Betz's law, adding Gaussian noise.
P = np.array([ rho * (V_3+np.random.normal())])

# For the exercise, least squares method is used to determine $\rho$.
rho = fit(V_3, P)
print(rho)
# [[[1.29200001]]]

plt.plot(V,
         [p[0] for p in P[0]],
         label='Betz\'s Law')
plt.legend()
plt.show()