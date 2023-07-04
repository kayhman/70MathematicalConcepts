import numpy as np

# This function computes
# the product of B by A.
def mult(A, B):
  nligsA, ncolsA = len(A), len(A[0])
  nligsB, ncolsB = len(B), len(B[0]);
  res = [[0] * ncolsB for i in range(nligsA)];
  for i in range(0, nligsA):
    for j in range(0, ncolsB):
      res[i][j] = 0
      for k in range(0, ncolsA):
          res[i][j] += A[i][k] * B[k][j]
  return res

# Each row of the matrix A
# contains the bike ride,
# the number of lengths,
# and the number of lifts.
A = [[15.2, 41, 51],
     [7.2,  0,  43],
     [10.2, 44, 63],
     [8.2,  0,  35],
     [5.2,  54, 43]]

# Each column contains the energy cost.
B = [[480.0], [100.0], [30.0]];

# The energy cost of each day
# is computed by multiplying A by B.
print(mult(A, B));
# > [[12926.0], [4746.0], [11186.0], [4986.0], [9186.0]]

# The matrix product
# is defined by default in numpy by {\em dot}.
print(np.array(A).dot(np.array([row[0] for row in B])))
# [12926.  4746. 11186.  4986.  9186.]