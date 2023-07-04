from math import pi, cos, sin

# This class implements a 3D rotation
# around a given axis.
class Rotation3D:
    def __init__(self, alpha, axis):
        self.axis = axis
        self.alpha = -alpha if axis == "y" else alpha
        self.coeffs = [1,
                       0, cos(alpha),
                       0, sin(alpha), cos(alpha)]

    # This function swaps coordinates
    # to change the rotation axis.
    def _swap(self, vec):
        if self.axis == "y":
            return[vec[1], vec[0], vec[2]]
        elif self.axis == "z":
            return[vec[2], vec[1], vec[0]]
        return vec

    # The actual rotation calculation is done here
    # An inversion is performed upstream and downstream
    # if the rotation axis is not $\vec{x}$.
    def __mul__(self, vec):
        vec = self._swap(vec)
        x = self.coeffs[0] * vec[0] - self.coeffs[1] * vec[1] - self.coeffs[3] * vec[2]
        y = self.coeffs[1] * vec[0] + self.coeffs[2] * vec[1] - self.coeffs[4] * vec[2]
        z = self.coeffs[3] * vec[0] + self.coeffs[4] * vec[1] - self.coeffs[5] * vec[2]
        return self._swap([x, y, z])

# By rotating by $pi$ around $\vec{x}$,
# point $P=(0, 1, 0)$ becomes $P_{pi}=(0, 0, 1)$.
R = Rotation3D(pi/2.0, 'x')
print(R * [0, 1, 0])
#> [0, 6.123233995736766e-17, 1.0]

# By rotating by $pi$ around $\vec{y}$,
# point $P=(0, 1, 0)$ remains unchanged
# because it is on the axis of rotation.
R = Rotation3D(pi/2.0, 'y')
print(R * [0, 1, 0])
#> [0.0, 1, 0.0]

# By rotating by $pi$ around $\vec{x}$,
# point $P=(0, 1, 0)$ becomes $P_{pi}=(1, 0, 0)$.
R = Rotation3D(pi/2.0, 'z')
print(R * [0, 1, 0])
#> [1.0, 6.123233995736766e-17, 0]
