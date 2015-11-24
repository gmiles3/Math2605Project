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
    #sets up w to alternate zeros and ones
    while i < n:
        if i % 2 == 0:
            w_t[i] = 1
        i += 1
    its = 0
    old_eigenvalue = 0
    eigenvalue = 0
    while its < max:
        new_v = matrixMult(matrix_a, v)
        eigenvalue = amax((dot(w_t, new_v)) / dot(w_t, v))
        if eigenvalue - old_eigenvalue < tolerance:
            break
        else:
            its += 1
            v = new_v
            old_eigenvalue = eigenvalue
    if its >= max:
        print "its are greater than max"
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
        num += (pow(vector[x],2))
    num = sqrt(num)
    num = 1/num
    return multiply(num, vector)


