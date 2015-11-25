from numpy import *
from powerMethod import *
import random
import xlwt
import matplotlib.pyplot as plt
from matplotlib import *
import matplotlib.cm as cm

# generates 1000 random 2x2 matrices
# @param n = number of matrices you want to create
def generate_matrices(n):
    matrixList = []
    for i in range(0, n):
        # generating random uniform matrices
        matrixList.append(matrix([[random.uniform(-2, 2), random.uniform(-2, 2)],
                                  [random.uniform(-2, 2), random.uniform(-2, 2)]]))
    return matrixList


# computes the inverse of matrices
def compute_inverse(A):
    a_inverse = matrix([[A[1, 1], multiply(-1, A[0, 1])],           # inverting the matrix
                        [multiply(-1, A[1, 0]), A[0, 0]]])

    det = multiply(A[0, 0], A[1, 1]) - multiply(A[0, 1], A[1, 0])   # calculating determinant
    if det == 0:                                                    # if det doesn't exist, runs again with a new matrix
        compute_inverse(generate_matrices(1))
    else:
        ad_bc = divide(1.0, det)                    # getting 1/determinant to normalize vector
        return multiply(ad_bc, a_inverse), det      # returns 1/determinant * inverse matrix


# computes the trace of the functio
def compute_trace(a):
    trace = 0                   # number to add each diagonal to
    for x in range(len(a)):     # for loop the length of the matrix
        trace += a[x, x]        # adding the current diagonal to the trace variable
    return trace


# trying to do scatter plot
def scatter_plot(det, trace, its):
    # example: http://matplotlib.org/examples/shapes_and_collections/scatter_demo.html
    # documentation: http://matplotlib.org/api/axes_api.html?highlight=scatter%20plot#matplotlib.axes.Axes.scatter
    # ^^for that link, ctrl+f scatter and it will get you to the documentation for this function
    # you need to finish filling in the arguments of the line below
    plt.scatter(det, trace)

    # also, my idea for the colors was to have a gradient getting darker as the number of
    # iterations got higher. you can change that if you want, but there's a good thread on
    # that methodology here:
    # http://stackoverflow.com/questions/28752727/map-values-to-colors-in-matplotlib

    # THANK YOU YOU'RE A SAINT




# running actual ish:
def main():
    matrix_list = generate_matrices(1000)  # generates 1000 random 2x2s
    starting_vector = matrix([[1],  # the "first guess" matrix for power method
                              [1]])
    failed = 1

    inverses = []  # all of these are the lists of data to add to
    largest_eigenvals = []
    smallest_eigenvals = []
    determinants = []
    num_its_a = []
    num_its_a_inverse = []
    trace_a = []
    trace_a_inverse = []

    # book = xlwt.Workbook()  # all of this stuff is just writing to excel
    # stuff = book.add_sheet("data")
    # stuff.write(0, 0, "determinant")
    # stuff.write(0, 1, "trace of A")
    # stuff.write(0, 2, "trace of a inverse")
    # stuff.write(0, 3, "number of iterations for A")
    # stuff.write(0, 4, "number of iterations for a inverse")

    while do_over != 0:
        do_over = 0
        for A in matrix_list:  # starting actual for loop to run power method etc
            A = matrix(A)  # everything goes to hell if I don't put this here so...

            inverse, det = compute_inverse(A)       # compute inverse and determinant
            inverses.append(inverse)                # add to inverse array
            determinants.append(det)                # add to determinant array

            # compute largest eigenvalue and number of iterations
            n = power_method(A, starting_vector, 0.00005, 100)      # running actual power method- returns tuple
            if n is not None:           # makes sure that power function didn't run out of iterations
                w = n[0]                # w = eigenvalue of matrix A
                num_its = n[2]          # number of iterations it took to get correct eigenvalue
                largest_eigenvals.append(w)  # add eigenvalue to correct array
                num_its_a.append(num_its)  # add to number of iterations to correct list

                # compute smallest eigenvalue and number of iterations for inverse matrix
                n2 = power_method(inverse, starting_vector, 0.00005, 100)
                if n2 is not None:          # makes sure that power function didn't run out of iterations
                    smallest_eigenvals.append(n2[0])        # adds eigenvalue to smallest eigenvalue list
                    num_its_a_inverse.append(n2[2])         # adds number of iterations to correct list

                # get trace of both
                trace_a.append(compute_trace(A))
                trace_a_inverse.append(compute_trace(inverse))
            else:                   # if power method fails, increments number of matrices to add to reach 1000
                failed += 1        # increments number of failed
        matrix_list = generate_matrices(failed)     # replaces arrays that failed to do over

    # writing info to excel spreadsheet
    # i = 1
    # for n in determinants:
    #     stuff.write(i, 0, n)
    #     i += 1
    # i = 1
    # for n in trace_a:
    #     stuff.write(i, 1, n)
    #     i += 1
    # i = 1
    # for n in trace_a_inverse:
    #     stuff.write(i, 2, n)
    #     i += 1
    # i = 1
    # for n in num_its_a:
    #     stuff.write(i, 3, n)
    #     i += 1
    # i = 1
    # for n in num_its_a_inverse:
    #     print n
    #     stuff.write(i, 4, n)
    #     i += 1
    #
    # book.save("trial.xls")

    # trying matploblib

    # SCATTERPLOTS- the scatter_plot function is on line 42!!!
    scatter_a = scatter_plot(determinants, trace_a, num_its_a)
    scatter_a_inverse = scatter_plot(determinants, trace_a, num_its_a_inverse)
    scatter_a.show()
    scatter_a_inverse.show()

main()


