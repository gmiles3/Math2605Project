from numpy import *
from sympy import *

def find_eigenvalues(matrix):
	y = Symbol('lambda')
	n = len(matrix)
	for i in range(0,n):
		matrix[i][i] = matrix[i][i] - y
	return solve(find_determinant(matrix))

def find_determinant(matrix):
	n = len(matrix)
	sign = 1
	total = 0
	if (n > 2):
		for i in range(0, n):
			seq = []
			for k in range(0, n):
				if k != i:
					seq.append(k)
			subm = [[matrix[r][c] for c in seq] for r in range(1, n)]
			total = total + (sign*matrix[0][i]*find_determinant(subm))
			sign = sign * -1 
		return total
	else:
		return (matrix[0][0]*matrix[1][1]) - (matrix[1][0]*matrix[0][1])

