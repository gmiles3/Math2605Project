import numpy as np


def pascal_generate(n):
    if n < 1:                       # if input size is not greater than 1, return
        return
    matrix = np.zeros((n, n))       # start with square matrix of 0's
    for i in range(1, n + 1):       # for each row
        for j in range(1, n + 1):   # for each col
            matrix[i - 1][j - 1] = factorial((i - 1) + (j - 1)) / (factorial(i - 1) * factorial(j - 1))     # use provided formula for calculating entry value
    b = np.zeros((n, 1))            # start with b matrix of 0's
    for i in range(0, n):           # for each row in b
        b[i][0] = 1 / (i + 1)       # calculate b entry
    return (matrix, b)              # return P and b


def factorial(num):
    toReturn = 1;                   # start with 1
    while num > 0:                  # while num is greater than 0, we keep multiplying
        toReturn = toReturn * num   # multiple by number
        num = num - 1               # decrement number
    return toReturn                 # return num!
