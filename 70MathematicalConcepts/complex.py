from sympy import symbols, diff, solve
import numpy as np
from cmath import sqrt
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# Definition of parameters a, b, and c
# and variable x.
x, a, b, c = symbols("x a b c")

# Definition of polynomial p.
p = a*x**2 + b*x + c

# Derivation of polynomial p
# with respect to x to obtain the minimum.
d = diff(p, x)

print(d)
#> 2ax + b

# Obtaining the value of x for which
# the polynomial reaches a minimum if a is positive
# and a maximum if a is negative.
min = solve(d, x)
print(min)
#> [-b/(2*a)

# Minimum reached at $x = \frac{-b}{2a}$.
print(p.subs(x, min))
#> c - b**2/(4*a)


# Plotting a polynomial with no real solution
# that does not intersect the x-axis.
a, b, c = 1, 0, 5

X = np.linspace(-10, 10, 100)
Y1 = [a * x**2 + b * x + c for x in X]

# Plotting a polynomial with no real solution
# with $a < 0$
# and thus located below the x-axis.
a, b, c = -1, 0, -5

Y2 = [a * x**2 + b * x + c for x in X]

plt.plot(X, Y1, label="P(x) with positive a")
plt.plot(X, Y2, label="P(x) with negative a")
plt.legend()
plt.show()

# Calculation of roots for a polynomial
# with no real solutions.
a, b, c = 1, 0, 5

delta = b**2 - 4 * a *c
print(delta)
#> - 10
x_1 = (-b + sqrt(delta)) / (2 * a)
x_2 = (-b - sqrt(delta)) / (2 * a)
print(x_1)
#> 2.23606797749979j
print(x_2)
#> -2.23606797749979j

# Verification of the validity of the factorization.
P = lambda x : a * x**2 + b * x + c
Pc = lambda x : (x - x_1) * (x - x_2)

# The polynomial is well-annulled for $x_1$.
print(P(x_1))
#> (-8.881784197001252e-16+0j)
print(Pc(x_1))
#> 0j

# Same for $x_2$.
print(P(x_2))
#> (-8.881784197001252e-16+0j)
print(Pc(x_2))
#> 0j


# The minimum $c - \frac{b^2}{4a} = 5$ is reached for $x = \frac{-b}{2a}$.
print(P(-b / (2*a)))
#> 5
print(Pc(-b / (2*a)))
#> 5+0j
