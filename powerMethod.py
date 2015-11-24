from numpy import *
from numpy import linalg as LA
from chezMatrixMult import matrixMult
from find_eigenvalues import find_eigenvalues

# returns a tuple: (approx eigenvalue, approx eigenvector, number of iterations)


# Performs Power Method
#
# @param matrix The matrix to perform power method on
# @param v initial guess vector to begin iterations with
# @param tolerance tolerance parameter to tell when approximation is close enough
# @param max = max number of iterations before function fails
# @return w, v, n = approx eigenvalue, approx eigenvector, number of iterations)
def power_method(matrix_a, v, tolerance, max):
    # x, y = LA.eig(matrix_a)
    x = find_eigenvalues(matrix_a)
    eigenval = amax(x)
    print "should be:", eigenval
    w = array([[1],
               [0]])
    w_transpose = transpose(w)
    pwr_eigenval = 0
    its = 0
    n = len(matrix_a)
    while its < max:
        new_vec = matrixMult(matrix_a, v)
        pwr_eigenval = amax((dot(w_transpose, new_vec) / dot(w_transpose, v)))
        if (eigenval - pwr_eigenval < tolerance):
            # "close enough" eigenvalue found
            break
        else:
            its += 1
            v = new_vec
    if its >= max:
        return None
    # calculate eigenvector
    eigenvector = 3 # something idk
    return (pwr_eigenval, eigenvector, its)





def main():
    #this way gives me errors in matrix multiplication
    arr1 = ([[3, 1], [2,4]])
    arr2 = ([[1],
            [1]])
    #this way gives me errors in find_eigenvalues
    arr1 = array([[3, 1], [2,4]])
    arr2 = array([[1],
            [1]])
    print power_method(arr1, arr2, 0.0005, 100)

main()