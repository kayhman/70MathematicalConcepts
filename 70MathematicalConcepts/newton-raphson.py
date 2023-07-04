# Numerically calculate the derivative of the function f at point x
# $f'(x) = \lim\limits_{d\rightarrow 0} \frac{f(x+d) - f(x)}{d}$.
def deriv(f, x, d=1e-3):
  return (f(x + d) - f(x)) / d


# Search for a solution of f(x) = 0 in the vicinity of $x_0$.
# $n$ is the number of iterations.
def raphson(f, x0, n=5):
  xi = x0  # xi contains the successive approximations.
  for i in range(0, n):
    d = -f(xi) / deriv(f, xi)
    xi = xi + d
  return xi


f = lambda x: x**3 - 2 * x - 5
r = raphson(f, 2)
print(r)
#-> 2.09455148154233
print(f(r))
# -> 3.8191672047105385e-14