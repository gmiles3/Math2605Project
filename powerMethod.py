from numpy import *

# returns a tuple: (approx eigenvalue, approx eigenvector, number of iterations)


# Performs Power Method
#
# @param matrix The matrix to perform power method on
# @param v initial guess vector to begin iterations with
# @param tolerance tolerance parameter to tell when approximation is close enough
# @param max = max number of iterations before function fails
# @return w, v, n = approx eigenvalue, approx eigenvector, number of iterations)
def power_method(matrix_a, v, tolerance, max):
    w_t = array([1,1])
    its = 0
    old_eigenvalue = 0
    eigenvalue = 0
    while its < max:
        new_v = matrixMult(matrix_a, v)
        print new_v
        eigenvalue = amax((dot(w_t, new_v)) / dot(w_t, v))
        if eigenvalue - old_eigenvalue < tolerance:
            break
        else:
            its += 1
            v = new_v
            old_eigenvalue = eigenvalue
    if its >= max:
        return None
    else:
        eigenvector = 2
        return eigenvalue, eigenvector, its





def matrixMult(A, B):
    A_Rows = A.shape[0]
    B_Cols = B.shape[1]
    if (A.shape[1] == B.shape[0]):
        newMat = zeros([A_Rows, B_Cols], dtype=float)
        for i in range(0,B_Cols):
            vecB = B[0:, i:i + 1]
            for j in range(0,A_Rows):
                vecA = A[j:j+1, 0:]
                newMat[j,i] = dot(vecA, vecB)
        return newMat

def main():

    arr1 = array([[3, 1], [2,4]])
    arr2 = array([[1],
                  [1]])
    print power_method(arr1, arr2, 0.005, 100)

main()