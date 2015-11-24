from numpy import *
from sympy import *
import string


def find_eigenvectors(matrix_a, eigenvalue):
    n = len(matrix_a)

    # alpha = string.ascii_lowercase[::-1]
    # s1 = tuple(alpha[:n])
    # # for a in s1:
    #
    # # s1 = list(s1)
    # print s1

    id = multiply(identity(n), eigenvalue)
    new = subtract(matrix_a, id)
    s1 = ()
    for i in range(n):
        s1 += Symbol('a_%d' % (i)),
    syms = list(s1)

    print syms
    print solve_linear_system(Matrix(new), a_0, a_1)
    # print "system solved" ,system_solved


def main():
    arr1 = array([[1,5], [-1,-5]])
    arr2 = array([[1],
                  [1],
                  [1]])
    print find_eigenvectors(arr1, 1)


main()
