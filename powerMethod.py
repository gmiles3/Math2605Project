import numpy as np


# power method.

# outputs:
# approximate eigenvalues
# approximate eigenvectors
# number of iterations needed to obtain that approximation

# A = nxn matrix, n >= 2, floating point real nums
# v = vector of n floating point real numbers- initial guess for eigenvector of A
# e = tolerance parameter (positive floating point real number)- when approximation is close enough
# N = max number of times to iterate the power method before quitting

# returns a tuple: (approx eigenvalue, approx eigenvector, number of iterations)
def power_method(A, v, ε, N):
    its = 0
    n = len(A)

