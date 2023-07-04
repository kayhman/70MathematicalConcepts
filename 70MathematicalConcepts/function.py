# The identity function is often found in mathematics.
# For example, to test a mathematical idea
# or a concept in the simplest case.
def identity(x):
    return x
from functools import reduce

# The square function is also very common.
# This follows from its importance in physics
# where it regularly appears in energy calculations.
def square(x):
    return x * x

# Example of the inverse function
# whose domain of definition is $\mathbb{R} \setminus 0$
# i.e., the set of real numbers without 0.
def inverse(x):
    return 1/x

# Polynomial functions are commonplace.
def polynome(A, x):
    return reduce(lambda a, b: a + b,
                  [a_i * x**i for i, a_i in enumerate(A)], 0)

print(identity(6))
#> 6
print(square(6))
#> 36
print(inverse(2))
#> 0.5

# The inverse of 0 is not calculable
# Python raises an exception.
#print(inverse(0))
#> ZeroDivisionError: division by zero
print(polynome([1, 2, 3], 1))
#> 6

# Iterative definition of the power function.
# $f : x \rightarrow x^n$
def iterative_power(x, n):
    # use of a power variable
    power = 1
    for i in range(0, n):
        power = power * x
    return power

# Functional definition of the power function.
# $f : x \rightarrow x^n$
def fonctional_power(x, n):
    return x * fonctional_power(x, n-1) if n != 1 else 1

print(iterative_power(2, 4))
#> 16
print(iterative_power(2, 4))
#> 16