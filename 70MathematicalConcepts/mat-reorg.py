from numpy import matrix

# The matrix to rearrange is
# matrix A.
A = matrix([[1, 1, 1],
            [2, 2, 2],
            [3, 3, 3]])

# P is the permutation matrix
# that will exchange row 1 with row 2
# and vice versa.
P = matrix([[0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]])

# Multiplying A by P.
print(P.dot(A))
#> [[2 2 2]
#>  [1 1 1]
#>  [3 3 3]]

A = matrix([[1, 2, 3],
            [1, 2, 3],
            [1, 2, 3]])

P = matrix([[0, 1, 0],
            [1, 0, 0],
            [0, 0, 1]])

print(A.dot(P))
#> [[2 1 3]
#>  [2 1 3]
#>  [2 1 3]]

print(P.dot(A.dot(P)))
#> [[2 1 3]
#>  [2 1 3]
#>  [2 1 3]]
