from numpy import *


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
    # sets up w to alternate zeros and ones, no matter the size it needs to be
    while i < n:
        if i % 2 == 0:
            w_t[i] = 1
        i += 1
    its = 0                 # keeps track of iteration number
    old_eigenvalue = 0      # declaring eigenvalue variable for denominator
    eigenvalue = 0          # declaring eigenvalue variable for numerator
    while its < max:                                           # loops while number of its is less than max allowed
        new_v = matrixMult(matrix_a, v)                        # multiplies matrix with vector to get next vector
        eigenvalue = amax(divide((dot(w_t, new_v)), dot(w_t, v)))       # (w^t dot v_(n + 1)) / (w^t dot v_n)
        if absolute(subtract(eigenvalue, old_eigenvalue)) < tolerance:  # checks to see if tolerance parameter is met
            break                           # if yes, leaves while loop, variables have been changed
        else:                               # if they're still too far apart:
            its += 1                        # increments iteration var
            v = new_v                       # sets v_n equal to v_(n+1)
            old_eigenvalue = eigenvalue     # sets old eigenvalue to new eigenvalue, so they can be compared next time
    if its >= max:                              # if iterations exceeded max allowed
        return None                             # return none
    else:                                       # if eigenvalue was found
        eigenvector = normalize(new_v)          # normalizing eigenvalue
        return eigenvalue, eigenvector, its     # returns eigenvalue, eigenvector, and # of iterations


# Normalizes a vector
#
# @param vector to normalize
# @return normalized vector
def normalize(vector):
    n = len(vector)                     # length of vector
    num = 0                             # number to add each element of the vector to
    for x in range(n):                  # going through each element of vector
        num += (pow(vector[x], 2))      # adding the element squared to the rest of the numbers (... + a^2)
    num = sqrt(num)                     # taking square root of the sum of all the elements squared
    num = 1 / num                       # dividing 1 by the square root of the number
    return multiply(num, vector)        # returning the normalized vector


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
