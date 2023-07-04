import numpy as np

def dot(u, v):
    scalar = 0
    for ui, vi in zip(u, v):
        scalar += ui * vi
    return scalar

u = [1, 2, 3]
v = [4, 5, 6]
s = dot(u, v)
print(s)
#> 32

# Verification using the library
# numpy
print(np.dot(u, v))
#> 32


# Using dot product
# to determine location
# of a point in relation to a plane

# To define a plane,
# a point and normal vector
# are needed
A = np.array([3, 0, 0])

n = np.array([1, 1, 0])
# Normalizing the vector
# to have ||n|| = 1.0
n = n / np.linalg.norm(n)
print(np.linalg.norm(n))
#> 0.99999999999

B = np.array([1, 1, 0])

# If B is on the other side
# of the plane,
# then the cosine of angle $\angle(\vec{AB}, \vec{n}) < 0$
AB = B - A
print(dot(AB, n))
#> -0.7071067811865475
# Point B is indeed
# on the other side of the plane.

# By translating it sufficiently
# along the normal, it crosses
# to the other side
C = AB + 4 * n

# The dot product becomes positive again
print(dot(C, n))
#> 3.2928932188134517