for the power method, there are four parameters:

matrix A (matrix to be evaluated)
vector v (starting "guess" of an eigenvector)
tolerance t (the tolerance parameter)
max max (the max number of iterations to run before failing)


and it outputs 3 things:
w = eigenvalue
v = eigenvector (normalized)
n = number of iterations it took

you should run it like this:


w, v, n = power_method(matrix_a, v, t, max)
