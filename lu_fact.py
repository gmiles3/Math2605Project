from numpy import *


def lu_fact(matA):
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
    return (i_matA, matA)       # return L and U
