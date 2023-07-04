import numpy as np
from sympy import symbols, expand, diff
from sympy.solvers import solve
import matplotlib.pyplot as plt

X = np.linspace(0, 5, 100)
p = lambda x: (x - 1) * (x - 3) * (x - 5)
Y = [p(x) for x in X]

# We create a variable: x
x = symbols('x')

print(diff(expand((x - 1) * (x - 3) * (x - 5))))
#> 3*x**2 - 18*x + 23
root = solve(diff(expand((x - 1) * (x - 3) * (x - 5))))
root = [float(r) for r in root]
print(root)
# [1.8452994616207485, 4.1547005383792515]
plt.plot(X, Y, label="y = (x-1)(x-2)(x-3)")
plt.plot(X, [p(root[0])] * len(X), '-.', label="maximum tangent")
plt.plot(X, [p(root[1])] * len(X), ':', label="minimum tangent")
plt.legend()
plt.show()

# The variation around an extremum
# is small.
delta = 1e-3
print(p(root[0] + delta) - p(root[0]))
#> -3.4631016152530947e-06

# For any other point
# this is not the case.
print(p(1 + delta) - p(1))
#> 0.007994000999999121

# By expressing this variation
# relatively to the variation of x
# the effect is even more striking.

print((p(root[0] + delta) - p(root[0])) / delta)
#> -0.0034631016152530947

# For any other point
# this is not the case.
print((p(1 + delta) - p(1)) / delta)
#> 7.994