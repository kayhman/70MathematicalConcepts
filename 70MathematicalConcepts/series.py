import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np


# Function calculating
# the series of terms u(k)
def series(u, n, start=0):
    return np.sum([u(k) for k in range(start, n)])


# Application to the series
# $S_k = \sum_{k=0}^n \left(\frac{1}{2}\right)^k$
N = 40
X = [n for n in range(0, N)]
Y = [series(lambda k : (1/2)**k, n) for n in X]
# Last term of the series
print(Y[-1])
# > 1.999999999996362
plt.plot(X, Y, label='Sum of (1/2)**k for k in [0, n]')
plt.legend()
plt.show()


# Application to the series
# $S_n = \sum_{k=1}^n \left(\frac{1}{k}\right)$
N = 1000
X = [n for n in range(1, N)]
Y = [series(lambda k : (1/k), n, 1) for n in X]
# Last term of the series
print(Y[-1])
# > 7.483469859549345
plt.plot(X, Y, label='Sum of 1/k for k in [0, n]')
plt.legend()
plt.show()