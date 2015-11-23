import numpy as np


def lu_fact(matrix):
    n = len(matrix)
    if n == 0:
        return
    i_matrix = np.identity(n)
    for col in range(0, n):
        i = 0
        for i in range(col, n):
            if matrix[i][col] != 0:
                break
        if matrix[i][col] != 0:
            for k in range(col + 1, n):
                if matrix[k][col] != 0:
                    multiple = matrix[k][col] / matrix[i][col]
                    i_matrix[k][col] = multiple
                    for c in range(0, n):
                        matrix[k][c] = matrix[k][c] - (matrix[i][c] * multiple)
    return (i_matrix, matrix)
