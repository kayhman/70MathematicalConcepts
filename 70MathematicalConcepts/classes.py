# Square root function is imported.
from math import sqrt

# Definition of a 2D triangle using the existing built-in base types in Python
# and calculation of its perimeter.

# A point is defined as a tuple of coordinates.
P0 = (0, 0)
P1 = (1, 0)
P2 = (0, 1)

# A triangle is defined as a tuple of three points.
T0 = (P0, P1, P2)

def perimeter(T):
    P0 = T[0]
    P1 = T[1]
    P2 = T[2]
    l0 = sqrt( (P0[0] - P1[0])**2 +  (P0[1] - P1[1])**2)
    l1 = sqrt( (P1[0] - P2[0])**2 +  (P1[1] - P2[1])**2)
    l2 = sqrt( (P2[0] - P0[0])**2 +  (P2[1] - P0[1])**2)
    return l0 + l1 + l2

print(perimeter(T0))
#> 3.414

# Definition using data structures.
# The code is more structured and easier to read.
class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def distance(self, other):
        return sqrt((self.x - other.x)**2 + (self.y - other.y)**2)


class Triangle():
    def __init__(self, P0, P1, P2):
        self.P0 = P0
        self.P1 = P1
        self.P2 = P2

    def perimeter(self):
        return self.P0.distance(self.P1) + self.P1.distance(self.P2) + self.P2.distance(self.P0)

P0 = Point(0, 0)
P1 = Point(1, 0)
P2 = Point(0, 1)

T0 = Triangle(P0, P1, P2)
print(T0.perimeter())
#> 3.414