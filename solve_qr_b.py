from numpy import *

def solve_qr_b(Q, R, b):
    n = len(Q)                                  # N is # of rows and cols
    y = zeros((n,1), float)                     # create vector of 0's to initialize y
    x = zeros((n,1), float)                     # create vector of 0's to initialize x
    y = matrixMult(Q.transpose(), b)            # y = Qt*b
    for i in range(n-1, -1, -1):                # for each row (each equation in system) going backwards
        subsum = 0                              # initialize sum to 0
        for k in range(i+1, n):                 # part of formula for backward substitution
            subsum += (R[i,k]*x[k,0])           # part of formula for backward substitution
        x[i,0] = (1/R[i,i])*(y[i,0] - subsum)   # part of formula for backward substitution
    return x