# Installation with pip: pip install numpy
# Importing library
import numpy as np
# np becomes an alias for Numpy.

# A vector is created like this
v = np.array([1, 2, 3])
print(v)
#> [1 2 3]

# Various statistical operations are available by default.
print(v.sum())
#> 6
print(v.mean())
#> 2.0
print(v.std())
#> 0.816496580927726

# A matrix is defined as follows
M = np.matrix([[1, 2, 3],
               [4, 5, 6],
               [7, 8, 9]])
print(M)
#> [[1 2 3]
#   [4 5 6]
#   [7 8 9]]
# Matrix vector product
print(M.dot(v))
# Matrix inversion
M = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])
print(np.linalg.inv(M))
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]