from sympy import symbols, solve, Matrix
import numpy as np

A = np.matrix([[2, -1, 0],
               [-1, 2, -1],
               [0, -1, 2]])

lambdas, eVs = np.linalg.eig(A)
# Eigenvalues.
print(lambdas)
#> [3.41421356 2.         0.58578644]
# Eigenvectors.
print(eVs)
#> [[-5.00000000e-01 -7.07106781e-01  5.00000000e-01]
#   [ 7.07106781e-01  4.05405432e-16  7.07106781e-01]
#   [-5.00000000e-01  7.07106781e-01  5.00000000e-01]]

# The inverse of the matrix
# containing the eigenvectors 
# is its transpose.
print(eVs * eVs.T)
#> [[1.00000000e+00 5.55111512e-17 0.00000000e+00]
#   [5.55111512e-17 1.00000000e+00 1.11022302e-16]
#   [0.00000000e+00 1.11022302e-16 1.00000000e+00]]

# The power iteration method
# allows to compute
# the eigenvector 
# associated with the largest eigenvalue.
def power(A, b, n_iter=100):
    for i in range(0, n_iter):
        b = A * b
        b = b / np.linalg.norm(b)
    return b

# Application to matrix A.
b = np.matrix([[1], [1], [1]])
eV1 = power(A, b)
x = A * eV1
# Recomputation of the associated eigenvalue.
lambda1 = x[0, 0] / eV1[0,0]

# The obtained vector is indeed the eigenvector.
print(eV1)
#> [[ 0.5       ]
#   [-0.70710678]
#   [ 0.5       ]]

# The eigenvalue is correct.
print(lambda1)
#> 3.414213562373095
# and $A e_1$
print(x)
#> [[ 1.70710678]
#  [-2.41421356]
#  [ 1.70710678]]
# is indeed equal to $\lambda_1 e_1$.
print(lambda1 * eV1)
#> [[ 1.70710678]
#   [-2.41421356]
#   [ 1.70710678]]

# The condition number of A
# is given by:
c = max(lambdas) / min(lambdas)
print(c)
#> 5.8284271247461845
# which is a good condition number.

# Computation of the eigenvalues
# using the determinant
# of the characteristic polynomial.
l = symbols("l")
I = np.eye(A.shape[0])

S = (Matrix(A) + l * Matrix(I))
lambdas = solve(S.det(), l)
print(lambdas)
#> [-3.41421356237309, -2.00000000000000, -0.585786437626905]
# These are the expected eigenvalues.
