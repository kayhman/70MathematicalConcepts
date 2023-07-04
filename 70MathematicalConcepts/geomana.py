`from math import pi, cos, sin
from numpy import linspace
from collections import namedtuple
import matplotlib.pyplot as plt
plt.style.use('grayscale')

# Create a class to manage points.
Point = namedtuple("Point", "x y")
# Positioning of points in a 2D plane.
O = Point(0.0, 0.0)
P0 = Point(1, 1)
P1 = Point(1.2, 1.2)

plt.scatter(O.x, O.y)
plt.scatter(P0.x, P0.y)
plt.scatter(P1.x, P1.y)

plt.annotate('0', (O.x, O.y))
plt.annotate('P0', (P0.x, P0.y))
plt.annotate('P1', (P1.x, P1.y))
plt.grid()
plt.show()

# Calculation of the points of a line
# whose slope is $a = 2$ and whose
# intersection with the y-axis is at $b = 1$.
a = 2
b = 1
D = lambda x : a * x + b


X = list(linspace(-2, 2, 100))
Y = [D(x) for x in X]
plt.plot(X, Y, label='Line D')
plt.grid()
plt.show()


# Calculation of the points of a logarithmic spiral
Theta = list(linspace(0, 8 * pi, 200))
a = 1
b = 1.3
X = [a*b**theta * cos(theta) for theta in Theta]
Y = [a*b**theta * sin(theta) for theta in Theta]
plt.plot(X, Y, label='Spiral S')
plt.grid()
plt.show()
`