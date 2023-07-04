import numpy as np

# We create here two vectors of dimension 3, A and B.
# These are also points.
A  = np.array([1, 0, 0])
B  = np.array([0, 1, 0])
print(A, B)
#> [1 0 0] [0 1 0]

# It is possible to add them together, in order to make S.
S = A + B
print(S)
#> [1 1 0]

# Multiplying vectors together is not possible,
# however, it is possible to multiply them by a scalar:
M = 0.5 * A
print(M)
#> [0.5 0 0]

# Multiplying two vectors together does not produce a vector,
# but rather a scalar. This is called the dot product.
s = A.dot(B)
print(s)
#> 0

# The calculation of the vector $\mathbf{v}$ between
# $A$ and $B$ is done as follows:
v = B - A
print(v)
#> [-1 1 0]