`from joblib import Parallel, delayed
import numpy as np

# The matrix A contains
# our system.
A = [[2, 1, 1, -1],
     [0, 1.5, -1, 0],
     [0, 0, 3, -1],
     [0, 0, 0, 1]]

# the column matrix B
# contains the right-hand side.
B = [0, 0, 2, 43]

# The Jacobi function
# calculates an approximate solution
# to our system.
def jacobi(A, B, maxIter):
    nligsA, ncolsA = len(A), len(A[0])
    X = [0.0] * ncolsA

    for j in range(0, maxIter):
        # Note the only difference with the Gauss-Seidel method
        # The new values of X are calculated from those of the previous iteration.
        X_c = X.copy()
        for i in range(0, ncolsA):
            X_c[i] = 0
            X[i] = (B[i] - np.dot([col for col in A[i]], X_c)) / A[i][i]
    return X

def parallel_jacobi(A, B, maxIter):
    nligsA, ncolsA = len(A), len(A[0])
    X = [0.0] * ncolsA

    def update_x_i(A, B, X, i):
        X[i] = 0
        return (B[i] - np.dot([col for col in A[i]], X)) / A[i][i]

    for j in range(0, maxIter):
        # Here, the loop has been transformed into independent calculations
        # executed in parallel.
        X = Parallel(n_jobs=8)(delayed(update_x_i)(A, B, X.copy(), i) for i in range(0, ncolsA))

    return X

# With only one iteration
# we are far from the result.
print(jacobi(A, B, 1))
# > [0.0, 0.0, 0.666, 43.0]
# With one more
# we get closer.
print(jacobi(A, B, 2))
# > [21.166666666666668, 0.4444444444444444, 15.0, 43.0]

# and two more
# are enough to find the
# exact solution.
print(jacobi(A, B, 4))
# > [9.0, 10.0, 15.0, 43.0]


# Same thing with the parallelized version.
print(parallel_jacobi(A, B, 4))
# > [9.0, 10.0, 15.0, 43.0] - the result is the same.