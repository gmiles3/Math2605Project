from numpy import *
from matrixMult import *
from pascal_generate import *


def lu_fact(matA):
    original = matA.copy()
    n = len(matA)                 # n is # of rows and cols
    i_matA = identity(n, float)       # i_matA will be transformed into L via all row operations that create U
    for col in range(0, n):         # for each col
        i = 0                       # initialize i
        for i in range(col, n):     # for each row
            if matA[i,col] != 0: # find pivot
                break
        if matA[i,col] != 0:
            for k in range(col + 1, n):     # for each entry beneath pivot
                if matA[k,col] != 0:     # if entry not already 0
                    multiple = matA[k,col] / matA[i,col]  # find multiple for eliminating entry
                    i_matA[k,col] = multiple # set corresponding i_matA entry to construct L
                    for c in range(0, n):   # for each entry along row, we want to apply same operation
                        matA[k,c] = matA[k,c] - (matA[i,c] * multiple)     # eliminate entry by multiplying pivot by multiple and subtracting
    derived_A = matrixMult(i_matA, matA)        # begin error calculation, compute L*U
    derived_A = derived_A - original            # compute LU - A
    current_max = 0                             # find norm by finding largest abs val of entries
    for col in range (0, n):                    # for each col
        for row in range(0, n):                 # for each row
            if abs(derived_A[row,col]) > current_max:       # if current abs val entry is bigger than max
                current_max = abs(derived_A[row, col])      # update
    return [i_matA, matA, current_max]       # return L, U, and error
