from math import exp, factorial
from sympy import integrate
import cProfile
import matplotlib.pyplot as plt

plt.style.use('grayscale')

# Simple implementation of factorial.
def trivial_factorial(n):
    prod = 1
    for k in range(1, n+1):
        prod *= k
    return prod


print(trivial_factorial(3))
#> 6

print(trivial_factorial(20))
#> 2 432 902 008 176 640 000

# Calculation of factorial for the first 20 integers.
X = list(range(0, 20))
Y = [trivial_factorial(x) for x in X]

plt.scatter(X, Y, label='Factorial')
plt.legend()
plt.show()


# Comparison with exponential function.
E = [exp(x) for x in X]

plt.scatter(X, Y, label='Factorial')
plt.plot(X, E, label='Exponential')
plt.legend()
plt.show()


# Recursive implementation of factorial
# using the fact that $n! = (n-1)!*n$.
def recursive_factorial(n):
    if n == 1:
        return 1
    return recursive_factorial(n-1) * n


print(recursive_factorial(20))

# Comparison of execution times between
# the trivial function and the Python built-in function.
cProfile.run('trivial_factorial(127000)')
#> 3.22 seconds
cProfile.run('factorial(127000)')
#> 0.192 seconds


# Bit size of the generated integer.
# The storage limit of a standard integer is quickly reached.
r = factorial(20)
print(r.bit_length())
#> 62

r = factorial(126000)
print(r.bit_length())
#> 1953057


# Verification of the generalization of factorial
# to real numbers with the $\Gamma$ function.
integrate(t**3 * exp(-t), t)
#> (-t**3 - 3*t**2 - 6*t - 6)*exp(-t)

-integrate(t**3 * exp(-t), t).subs({t:0})
#> 6
