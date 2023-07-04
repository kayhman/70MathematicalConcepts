# This class implements the mechanism of automatic differentiation.
class AutoReal:
    # At initialization, two fields are filled for this object,
    # its value $val$ and its derivative $der$.
    def __init__(self, val, der):
        self.val = val
        self.der = der

    # Addition follows the formula:
    # $(u+v)' = u' + v'$
    def __add__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val + b.val, self.der + b.der)

    # Subtraction follows the formula:
    # $(u-v)' = u' - v'$
    def __sub__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val - b.val, self.der - b.der)

    # Multiplication follows the formula:
    # $(u*v)' = u' * v + u * v'$
    def __mul__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val * b.val, self.val * b.der + self.der * b.val)

    # Division follows the formula:
    # $(\frac{u}{v})' = \frac{u' * v - u * v'}{v^2}$
    def __div__(self, b):
        if isinstance(b, (float, int)):
            b = AutoReal(b, 0)
        return AutoReal(self.val / b.val, (self.der * b.val - self.val * b.der) / (b.val * b.val))

    def __str__(self):
        return f'Value: {self.val}, Derivative: ({self.der})'


p = lambda x: (x - 1) * (x - 3) * (x - 5)
# The derivative of this polynomial, as seen on page \pageref{extremum}, is:
p_prime = lambda x: 3 * x ** 2 - 18 * x + 23
x = AutoReal(3, 1)

# The derivative at $x = 3$ will be computed automatically,
# at the same time as the value:
print(p(x))
#> Value: 0, Derivative: (-4)
# The result obtained with the formula is the same.
print(p_prime(3))
#> -4