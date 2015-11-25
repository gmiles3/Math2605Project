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
    n = len(matrix_a)
    w_t = zeros(n)
    i = 0
    # sets up w to alternate zeros and ones
    while i < n:
        if i % 2 == 0:
            w_t[i] = 1
        i += 1
    its = 1
    old_eigenvalue = 0
    eigenvalue = 0
    while its < max:
        new_v = matrixMult(matrix_a, v)
        eigenvalue = amax(divide((dot(w_t, new_v)), dot(w_t, v)))
        if absolute(subtract(eigenvalue, old_eigenvalue)) < tolerance:
            break
        else:
            its += 1
            v = new_v
            old_eigenvalue = eigenvalue
    if its >= max:
        return None
    else:
        eigenvector = normalize(new_v)
        return eigenvalue, eigenvector, its


# Normalizes a vector
#
# @param vector to normalize
# @return normalized vector
def normalize(vector):
    n = len(vector)
    num = 0
    for x in range(n):
        num += (pow(vector[x], 2))
    num = sqrt(num)
    num = 1 / num
    return multiply(num, vector)


def matrixMult(A, B):
    A_Rows = A.shape[0]
    B_Cols = B.shape[1]
    if (A.shape[1] == B.shape[0]):
        newMat = zeros([A_Rows, B_Cols], dtype=float)
        for i in range(0, B_Cols):
            vecB = B[0:, i:i + 1]
            for j in range(0, A_Rows):
                vecA = A[j:j + 1, 0:]
                newMat[j, i] = dot(vecA, vecB)
        return newMat


# #test cases
# def main():
#     starting_vector = matrix([[1],
#                               [1]])
#
#     new_matrix = matrix([[0, 1],
#                          [-2, -3]])
#     w, v, n = power_method(new_matrix, starting_vector, 0.0005, 100)
#     print "eigenvalue", w
#     print "eigenvector: ", v
#     print "number of iterations: ", n
#
# main()