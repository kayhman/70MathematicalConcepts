# Calculation of position at time t
# if displacement occurs at constant speed V.
def position(V, t):
    return V * t

# Generic function to calculate the derivative
# of a function f at a point x
# by taking h sufficiently small.
def derivative(f, x, h=1e-3):
    return (f(x+h) - f(x)) / h

# Calculation of instantaneous velocity at time t = 15,
# for a constant speed of 5.
print(derivative(lambda x : position(5, x), 15))
# > 4.9999999999954525