from sympy import symbols, expand, diff

x, a, b, c = symbols('x a b c')

p = a*x**2 + b * x + c
print(p)
#> a*x**2 + b*x + c

# Sympy supports differentiation.
# Here with respect to x.
print(diff(p, x))
#> 2*a*x + b

# Differentiation with respect to a.
print(diff(p, a))
#> x**2

# Sympy can also expand expressions.
expand(p * p)
#> a**2*x**4 + 2*a*b*x**3 + 2*a*c*x**2 + b**2*x**2 + 2*b*c*x + c**2
