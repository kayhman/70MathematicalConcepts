from sympy import symbols, factor, re, im, simplify
import matplotlib.pyplot as plt
from math import sqrt, atan2

# Using sympy,
# the symbols ra, rb, ia, and ib
# are defined.
ra, rb = symbols('ra rb', real=True)
ia, ib = symbols('ia ib', imaginary=True)

a = ra + ia
b = rb + ib

# sympy also supports symbolic computation
# with complex numbers.
print(simplify(re(a * b)))
#> ia*ib + ra*rb
print(simplify(im(a * b)))
#> (ia*rb + ib*ra)

# Calculation of the polar representation
# of complex numbers.
c = 0.5 + 0.5j
# Calculation of the radius r.
r = sqrt(c.imag**2 + c.real**2)
# and the angle theta.
theta = atan2(c.imag, c.real)
print(r)
#> 0.7071067811865476
print(theta)
#> 0.7853981633974483

# Polar plot with matplotlib.
plt.axes(projection = 'polar')
plt.polar(theta, r, 'k.', markersize=40)
plt.show()

# By multiplying c by itself
# its radius will be multiplied by r
# and its angle doubled.
c2 = c * c
r2 = sqrt(c2.imag**2 + c2.real**2)
theta2 = atan2(c2.imag, c2.real)
plt.axes(projection = 'polar')
plt.polar(theta, r, 'k.', markersize=40, label='c')
plt.polar(theta2, r2, 'k.', markersize=40, label='c*c')
plt.show()
