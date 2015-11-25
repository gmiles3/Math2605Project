from numpy import *

def solve_lu_b(L, U, b):
    n = len(L)                                  # N is # of rows and cols
    y = zeros((n,1), float)                     # create vector of 0's to initialize y
    x = zeros((n,1), float)                     # create vector of 0's to initialize x
    for i in range(0, n):                       # for each row (each equation in system)
        subsum = 0                              # initialize sum to 0
        for k in range(0, i):                   # part of formula for forward substitution
            subsum += (L[i,k]*y[k,0])           # part of formula for forward substitution
        y[i,0] = (1/L[i,i])*(b[i,0] - subsum)   # part of formula for forward substitution
    for i in range(n-1, -1, -1):                # for each row (each equation in system) going backwards
        subsum = 0                              # initialize sum to 0
        for k in range(i+1, n):                 # part of formula for backward substitution
            subsum += (U[i,k]*x[k,0])           # part of formula for backward substitution
        x[i,0] = (1/U[i,i])*(y[i,0] - subsum)   # part of formula for backward substitution
    return x

