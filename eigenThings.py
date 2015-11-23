import numpy as np
from sympy import *

def testEigenvalues(A):
    a = A[[0],[0]]
    b = A[[0],[1]]
    c = A[[1],[0]]
    d = A[[1],[1]]


    #w,v = LA.eig(A)
    y = Symbol('lambda')
    part1 = (a*d)-(y*a)-(y*d)+(y*y)
    part2 = b*c
    quad = part1-part2

    return solve(quad)



# test case for 2x2 matrices
def main():

    matrixA = np.array([[1,-2],
                        [1,4]])

    print testEigenvalues(matrixA)
    print ("should be lambda = 2,3")

main()