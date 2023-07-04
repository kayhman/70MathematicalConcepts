import matplotlib.pyplot as plt
plt.style.use('grayscale')
import numpy as np

# In Euclidean geometry
# distance and angle are preserved.

# Creation of a 30° rotation matrix.
theta = np.radians(90)
c, s = np.cos(theta), np.sin(theta)
R = np.mat([(c, -s), (s, c)])

A = np.array([[0], [0]])
B = np.array([[0], [1]])
C = np.array([[1], [0]])

# Distance between A, B and C
print(np.linalg.norm(B - A))
#> 1.0
print(np.linalg.norm(C - A))
#> 1.0
print(np.linalg.norm(C - B))
#> 1.41421


# Rotation of points A, B and C
Ar = R * A
Br = R * B
Cr = R * C

print(Ar)
#> [[0.]
#>  [0.]]
print(Br)
#> [[-1.000000e+00]
#>  [ 6.123234e-17]]
print(Cr)
#> [[6.123234e-17]
#>  [1.000000e+00]]

# Distance between A, B and C
# after rotation.
# They remain unchanged.
print(np.linalg.norm(Br - Ar))
#> 1.0
print(np.linalg.norm(Cr - Ar))
#> 1.0
print(np.linalg.norm(Cr - Br))
#> 1.41421

# Translation of A, B and C
# according to vector T.
T = np.array([[1], [2]])
At = A + T
Bt = B + T
Ct = C + T


# Distance between A, B and C
# after translation.
# They remain unchanged.
print(np.linalg.norm(Bt - At))
#> 1.0
print(np.linalg.norm(Ct - At))
#> 1.0
print(np.linalg.norm(Ct - Bt))
#> 1.41421

# Display of the triangle
# and its translated copy.
triangle = plt.Polygon([A.reshape(2), B.reshape(2), C.reshape(2)])
triangleT = plt.Polygon([At.reshape(2), Bt.reshape(2), Ct.reshape(2)])
fig, ax = plt.subplots()

ax.add_patch(triangle)
ax.add_patch(triangleT)
ax.set_xlim([0, 3])
ax.set_ylim([0, 3])
plt.show()