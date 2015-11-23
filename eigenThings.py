import numpy as np
from sympy import *

def test_eigenvalues(A):
    n = len(A)

    y = Symbol('lambda')
    id = np.identity(n) * y
    B = np.subtract(A,id)
    print ("b: ", B)

    if len(A) == 2:
        a = A[[0],[0]]
        b = A[[0],[1]]
        c = A[[1],[0]]
        d = A[[1],[1]]
        part1 = (a*d)-(y*a)-(y*d)+(y*y)
        part2 = b*c
        quad = part1-part2

        return solve(quad)
    else:
        #finding the determinant- should be an equation
        det = find_determinant(B,0,0)
        #getting an error here because of some issue in find determinant- getting a null output
        return solve(det)

# finds determinant of matrix
#
# @param B matrix to find determinant of
# @param r row of matrix currently on
# @param quad quadratic eqn to add to and eventually return
# @return
def find_determinant(B, r, quad):
    if len(B) > 2:
        while r < len(B):
            new = step_down(B, r, 0)
            quad += B[r][0] * find_determinant(new, r + 1, quad)
            c = 1
            while c < len(B[0]):
                cross = B[r][c]
                new = step_down(B, r, c)
                quad -= cross * find_determinant(new, r + 1, quad)
                c += 1
            r += 1
    else:
        print ("last round", quad)
        a = B[[0],[0]]
        b = B[[0],[1]]
        c = B[[1],[0]]
        d = B[[1],[1]]

        quad += (a*d - b*c)

        return quad

# gets minor matrix
#
# @param matrix to find minor of
# @param r row to eliminate
# @param c column to eliminate
# @return sub-matrix or minor matrix
def step_down(A, r, c):
    return A[np.array(range(r) + range(r + 1, A.shape[0]))[:, np.newaxis],
               np.array(range(c) + range(c + 1, A.shape[1]))]






# test case for 3x3
def main():

    matrixA = np.array([[1,2,1],
                        [1,3,2],
                        [2,1,4]])

    print test_eigenvalues(matrixA)
    print ("should be: 5")

main()