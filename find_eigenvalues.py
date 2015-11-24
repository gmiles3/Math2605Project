from numpy import *
from sympy import *

def find_eigenvalues(matrix):
	y = Symbol('lambda')					# y will be unknown lambda
	n = len(matrix)							# n is # of rows and cols
	for i in range(0,n):					# for each col
		matrix[i][i] = matrix[i][i] - y		# subtract lambda from each diagonal entry
	return solve(find_determinant(matrix))	# call determinant function, use solve function to solve quadratic

def find_determinant(matrix):
	n = len(matrix)					# n is # of rows and cols
	sign = 1						# alternating sign coefficient for cofactor expansion
	total = 0						# running total of determinant calculations
	if (n > 2):						# if bigger than trivial 2x2 determinant
		for i in range(0, n):		# for each col
			seq = []				# empty list to determine which cols to use
			for k in range(0, n):	# for each col
				if k != i:			# if the current top col entry will be coefficient of determinant, don't add
					seq.append(k)	# add every other col coefficient
			subm = [[matrix[r][c] for c in seq] for r in range(1, n)]	# retrieves sub matrix of all entries not in col and row eliminated
			total = total + (sign*matrix[0][i]*find_determinant(subm))	# recursively call determinant on submatrix, multiply by coefficient and sign
			sign = sign * -1 		# change sign coefficient
		return total				# return running total of determinant calculation
	else:
		return (matrix[0][0]*matrix[1][1]) - (matrix[1][0]*matrix[0][1])	# else if trivial 2x2, do a*d - b*c

mat = [[1,-7],[-2,-3]]
print(find_eigenvalues(mat))

def find_norm(matrix):
	matrix = matrixMult(matrix.transpose(), matrix)
	lambdas = find_eigenvalues(matrix)
	max_lambda = 0
	for l in lambdas:
		if abs(l) > max_lambda:
			max_lambda = l
	return sqrt(max_lambda)
