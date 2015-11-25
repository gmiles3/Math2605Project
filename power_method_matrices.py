from numpy import *
from powerMethod import *
import random
import xlwt

# generates 1000 random 2x2 matrices
# THIS IS WHERE THE PROBLEM IS I'M PRETTY SURE
def generate_matrices(n):
    matrixList = []
    for i in range(0, n):
        # doesn't work- get error: "nonetype' object is not iterable
        # strange because sometimes a few of them will go through the loop
        # and then it will stop on one randomly- maybe the random.uniform
        # sometimes outputs weird numbers?
        matrixList.append(matrix([[random.uniform(-2, 2), random.uniform(-2, 2)],
                                  [random.uniform(-2, 2), random.uniform(-2, 2)]]))

        # strangely, this way works- it recognizes hard-coded numbers,
        # but not the randomly selected ones.


        # matrixList.append(matrix([[0, 1],
        #                  [-2, -3]]))
    return matrixList



#computes the inverse of the functions- works fine

def compute_inverse(A):
    a_inverse = matrix([[A[1,1], multiply(-1,A[0,1])],
                        [multiply(-1, A[1,0]), A[0,0]]])

    det = multiply(A[0,0], A[1,1]) - multiply(A[0,1], A[1, 0])
    if det == 0:
        compute_inverse(generate_matrices(1))
    else:
        ad_bc = divide(1.0, det)
        return multiply(ad_bc, a_inverse), det

# computes the trace of the function- works fine
def compute_trace(a):
    trace = 0
    for x in range(len(a)):
        trace += a[x,x]
    return trace



# running actual ish:
def main():


    matrix_list = generate_matrices(1000)               #generates 1000 random 2x2s
    starting_vector = matrix([[1],                      # the "first guess" matrix for power method
                              [1]])



    inverses = []                                       # all of these are the lists of data to add to
    largest_eigenvals = []
    smallest_eigenvals = []
    determinants = []
    num_its_a = []
    num_its_a_inverse = []
    trace_a = []
    trace_a_inverse = []



    book = xlwt.Workbook()                              #all of this stuff is just writing to excel
    stuff = book.add_sheet("data")
    stuff.write(0, 0, "determinant")
    stuff.write(0, 1, "trace of A")
    stuff.write(0, 2, "trace of a inverse")
    stuff.write(0, 3, "number of iterations for A")
    stuff.write(0, 4, "number of iterations for a inverse")


    for A in matrix_list:                               #starting actual for loop to run power method etc
        A = matrix(A) #trying to fix the nonetype error- probably doesn't do anything

        #  compute inverse and determinant
        inverse, det = compute_inverse(A)
        inverses.append(inverse) #add to inverse array
        determinants.append(det) #add to determinant array


        # compute largest eigenvalue and number of iterations: this is where issues begin
        w, v, n = power_method(A, starting_vector, 0.00005, 100)
        largest_eigenvals.append(w) #add eigenvalue to correct array
        num_its_a.append(n) #add to number of iterations list


        # compute smallest eigenvalue and number of iterations
        w2, v2, n2 = power_method(inverse, starting_vector, 0.00005, 100)
        smallest_eigenvals.append(w2)
        num_its_a_inverse.append(n2)


        #get trace of both
        trace_a.append(compute_trace(A))
        trace_a_inverse.append(compute_trace(inverse))


    # writing info to excel- this works you can ignore it
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
