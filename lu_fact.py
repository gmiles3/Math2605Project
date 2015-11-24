import numpy as np


def lu_fact(matrix):
    n = len(matrix)                 # n is # of rows and cols
    i_matrix = np.identity(n)       # i_matrix will be transformed into L via all row operations that create U
    for col in range(0, n):         # for each col
        i = 0                       # initialize i
        for i in range(col, n):     # for each row
            if matrix[i][col] != 0: # find pivot
                break
        if matrix[i][col] != 0:
            for k in range(col + 1, n):     # for each entry beneath pivot
                if matrix[k][col] != 0:     # if entry not already 0
                    multiple = matrix[k][col] / matrix[i][col]  # find multiple for eliminating entry
                    i_matrix[k][col] = multiple # set corresponding i_matrix entry to construct L
                    for c in range(0, n):   # for each entry along row, we want to apply same operation
                        matrix[k][c] = matrix[k][c] - (matrix[i][c] * multiple)     # eliminate entry by multiplying pivot by multiple and subtracting
    return (i_matrix, matrix)       # return L and U
