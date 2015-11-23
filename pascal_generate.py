import numpy as np


def pascal_generate(n):
    if n < 1:
        return
    matrix = np.zeros((n, n))
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            matrix[i - 1][j - 1] = factorial((i - 1) + (j - 1)) / (factorial(i - 1) * factorial(j - 1))
    b = np.zeros((n, 1))
    for i in range(0, n):
        b[i][0] = 1 / (i + 1)
    return (matrix, b)


def factorial(num):
    toReturn = 1;
    while num > 0:
        toReturn = toReturn * num
        num = num - 1
    return toReturn
