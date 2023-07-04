import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np

# Definition of the 3 points of the triangle.
A = np.array([0, 0])
B = np.array([3, 0])
C = np.array([0, 4])

# Point P is inside the triangle.
P = np.array([2, 1])

# Point P2 is outside the triangle.
P2 = np.array([2, 2])

# Calculation of the surface area of triangle ABC.
sABC = np.linalg.det(np.matrix([B - A, C - A]))

def barycentric_coordinates(A, B, C, P):
    # Calculation of the surface area of triangles
    # PBC, APC and ABP.
    sPBC = np.linalg.det(np.matrix([B - P, C - P]))
    sAPC = np.linalg.det(np.matrix([C - P, A - P]))
    sABP = np.linalg.det(np.matrix([A - P, B - P]))

    # The barycentric coordinates
    # are the ratios between the surface areas
    # of the small triangles and the large one.
    a = sPBC / sABC
    b = sAPC / sABC
    c = sABP / sABC
    return a, b, c
a, b, c = barycentric_coordinates(A, B,
                                  C, P)
print(a, b, c)
#> 0.08333333333333333 0.6666666666666665 0.24999999999999997

# The relation $\sum \lambda_i\vec{BP_i} = \vec{0}$
# is respected.
Pb = a * (A - P) + b * (B - P) + c * (C - P)
print(Pb)
#> [-5.55111512e-17  0.00000000e+00]

# Same thing for point $P_2$.
a, b, c = barycentric_coordinates(A, B, C, P2)
# One of the coordinates is negative,
# the point is outside the triangle.
print(a, b, c)
#> -0.16666666666666666 0.6666666666666665 0.5


# Plot the triangle
# and the interior and exterior points.
points = [A, B, C]
trg = plt.Polygon(points)
plt.gca().add_patch(trg)
plt.scatter([pts[0] for pts in points], [pts[1] for pts in points])
plt.scatter([pts[0] for pts in [P]], [pts[1] for pts in [P]])
plt.scatter([pts[0] for pts in [P2]], [pts[1] for pts in [P2]])
plt.annotate('P', P)
plt.annotate('P2', P2)
plt.show()