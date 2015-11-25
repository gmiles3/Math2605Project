from numpy import *
from powerMethod import *
import xlwt


def generate_matrices(n):
    matrixList = []
    for i in range(0, n):

        #gives nonetype error
        matrixList.append(matrix([[random.uniform(-2, 2), random.uniform(-2, 2)],
                                  [random.uniform(-2, 2), random.uniform(-2, 2)]]))

        #does not give nonetype error
        # matrixList.append(matrix([[0, 1],
        #                         [-2, -3]]))


        print matrixList[i]
    return matrixList


def compute_inverse(A):
    a_inverse = matrix([[A[1,1], multiply(-1,A[0,1])],
                        [multiply(-1, A[1,0]), A[0,0]]])

    det = multiply(A[0,0], A[1,1]) - multiply(A[0,1], A[1, 0])
    if det == 0:
        compute_inverse(generate_matrices(1))
    else:
        ad_bc = divide(1.0, det)
        return multiply(ad_bc, a_inverse), det


def compute_trace(a):
    trace = 0
    for x in range(len(a)):
        trace += a[x,x]
    return trace


def main():
    matrix_list = generate_matrices(1000)
    print "DONE CREATING MATRICES ----------------------"
    starting_vector = matrix([[1],
                              [1]])
    inverses = []
    largest_eigenvals = []
    smallest_eigenvals = []
    determinants = []
    num_its_a = []
    num_its_a_inverse = []
    trace_a = []
    trace_a_inverse = []
    book = xlwt.Workbook()
    stuff = book.add_sheet("data")
    stuff.write(0, 0, "determinant")
    stuff.write(0, 1, "trace of A")
    stuff.write(0, 2, "trace of a inverse")
    stuff.write(0, 3, "number of iterations for A")
    stuff.write(0, 4, "number of iterations for a inverse")
    for A in matrix_list:
        # compute inverse and determinant
        inverse, det = compute_inverse(A)
        inverses.append(inverse)
        determinants.append(det)
        # compute largest eigenvalue and number of iterations
        w, v, n = power_method(A, starting_vector, 0.00005, 100)
        largest_eigenvals.append(w)
        num_its_a.append(n)
        # compute smallest eigenvalue and number of iterations
        w2, v2, n2 = power_method(inverse, starting_vector, 0.00005, 100)
        smallest_eigenvals.append(w2)
        num_its_a_inverse.append(n2)
        #get trace of both
        trace_a.append(compute_trace(A))
        trace_a_inverse.append(compute_trace(inverse))


    i = 1
    for n in determinants:
        stuff.write(i, 0, n)
        i += 1
    i = 1
    for n in trace_a:
        stuff.write(i, 1, n)
        i += 1
    i = 1
    for n in trace_a_inverse:
        stuff.write(i, 2, n)
        i += 1
    i = 1
    for n in num_its_a:
        stuff.write(i, 3, n)
        i += 1
    i = 1
    for n in num_its_a_inverse:
        stuff.write(i, 4, n)
        i += 1

    book.save("trial.xls")


main()
