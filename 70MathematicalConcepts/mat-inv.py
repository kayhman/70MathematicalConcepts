import numpy as np

# The cofactors are the $i, j$ elements
# of the cofactor matrix of A.
def cofactor(A, i, j):
    C_ij = A.copy()
    C_ij[:, j] = 0
    C_ij[i, j] = 1
    return np.linalg.det(C_ij)

# The cofactor matrix is built out of the cofactors.
def comatrix(A):
    C = np.zeros(A.shape)
    for i in range(0, A.shape[0]):
        for j in range(0, A.shape[1]):
            C[i, j] = cofactor(A, i, j)
    return C

# The inversion is directly computed
# using the formula given above.
def inv(A):
    return 1.0 / np.linalg.det(A) * comatrix(A).T


A = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])

# The inverse is the expected one.
print(inv(A))
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]

# It can easily be checked with numpy.
print(np.linalg.inv(A))
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]

print(inv(A) * A)
#> [[ 1.00000000e+00  1.11022302e-16  0.00000000e+00]
#   [ 0.00000000e+00  1.00000000e+00  0.00000000e+00]
#   [-5.55111512e-17  1.11022302e-16  1.00000000e+00]]


# Computing the inverse by solving
# for each column of the identity matrix.
I = np.eye(A.shape[0])
inv_1 = np.linalg.solve(A, I[:, 0])
# The result is the expected first column.
print(inv_1)
#> [0.75 0.5  0.25]

inv_2 = np.linalg.solve(A, I[:, 1])
# The result is the expected second column.
print(inv_2)
#> [0.5 1.  0.5]

inv_3 = np.linalg.solve(A, I[:, 2])
# The result is the expected third column.
print(inv_3)
#> [0.25 0.5  0.75]
inv = np.matrix([inv_1, inv_2, inv_3]).T

# and the resulting matrix is well the inverse.
print(inv)
#> [[0.75 0.5  0.25]
#   [0.5  1.   0.5 ]
#   [0.25 0.5  0.75]]
