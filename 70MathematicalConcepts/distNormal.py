import numpy as np
from math import pi, sqrt, exp
import matplotlib.pyplot as plt

# Definition of the normal distribution function
f = lambda sigma, mu, x: 1.0 / (sigma * sqrt(2*pi)) * exp(-0.5 * ((x - mu)/sigma)**2)

# Plotting the standard normal distribution with $\mu = 0$ and $\sigma = 1$
sigma = 1.0
mu = 0

X = np.linspace(-5, 5, 100)
Y = [f(sigma, mu, x) for x in X]

plt.plot(X, Y)
plt.show()

# Definition of the multivariate Gaussian version, 
# used to calculate $\mathbb{P}(A \cap B)$
mnv = lambda Sigma, Mu, x: 1.0/np.linalg.det(2*pi*Sigma)**2 * exp(-0.5 * ((x - Mu).T * np.linalg.inv(Sigma) * (x - Mu)))

sigma_A = 1.0
mu_A = 0
sigma_B = 1.0
mu_B = 0

Sigma = np.matrix([[sigma_A, 0], [0, sigma_B]])
Mu = np.matrix([[mu_A], [mu_B]])

x_b = 0
X = np.linspace(-7, 7, 100)
Y_AnB = [mnv(Sigma, Mu, np.array([[x], [x_b]])) for x in X]
Y_B = [f(sigma_B, mu_B, x_b) for x in X]

# The distribution for the conditional probability is calculated here
Y_cond = [(yanb) / yb for yanb, yb in zip(Y_AnB, Y_B)]

# And displayed here.
plt.plot(X, Y_cond)
plt.show()