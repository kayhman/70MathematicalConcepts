from sympy import symbols, expand, factor

# We create three variables: t, x, and y.
t, x, y = symbols('t x y')

# Here, we apply algebraic rules to simplify the expression $t^2 + t * (t + t^3)$.
print(expand(t**2 + t * (t + t**3)))

# > t**4 + 2*t**2

print(factor(t**2 + t * (t + t**3)))

# > t**2*(t**2 + 2)
