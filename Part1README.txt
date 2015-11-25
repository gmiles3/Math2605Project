Our project utilizes the numpy library for creating and manipulating data structures such as matrices. TO RUN OUR CODE, YOU MUST HAVE NUMPY INSTALLED. Use of other data structures in the place of this numpy matrices (such as lists) will result in program failure and some perplexing error messages. Please instantiate all matrices in the following manner when passing in to functions:
	a_matrix = matrix([[a, b, c], [d, e, f], [g, h, i]], float)
This may seem like overkill, but our group had huge problems trying to integrate code because of slight differences in matrix representation.

The following functions are included in part 1:

pascal_generate(n) [helper function]
	- Input: nonnegative integer
	- Output: an array of NxN Pascal matrix P and vector b (P -> array[0] ; b -> array[1])

lu_fact(matrix)
	- Input: square numpy matrix
	- Output: an array of lower-triangular matrix L, upper-triangular matrix U, and error of factorization (L -> array[0] ; U -> array[1] ; error -> array[2])

solve_lu_b(L, U, b)
	- Input: lower-triangular numpy matrix L, upper-triangular numpy matrix U, and Nx1 numpy matrix b
	- Output: the Nx1 numpy matrix x solution for Ax=b, where A = LU
	- #NOTE: when inputing a matrix b, if you are using fractions (such as is the case for the Pascal matrices Px=b), you must add a period to the entries to cast them as floating point numbers. IF YOU DO NOT, THE PROGRAM WILL NOT OUTPUT THE CORRECT X.
	Ex: b = matrix([1], [1./2.], [1./3.], [1./4.], ..., )

matrixMult(A, B) [helper function]
	- Input: numpy matrix A and matrix B (where #cols of A = #rows of B)
	- Output: the dot product of the two input matrices

qr_fact_givens(matrix)
	- Input: square numpy matrix
	- Output: an array of resulting orthogonal matrix Q, upper-triangular matrix R, and error of factorization from use of Givens Rotation matrices (Q -> array[0] ; R -> array[1] ; error -> array[2])

solve_qr_b(Q, R, b)
	- Input: orthogonal numpy matrix Q, upper-triangular matrix R, and Nx1 numpy matrix b
	- Output: the Nx1 numpy matrix x solution for Ax=b, where A = QR
	- #NOTE: when inputing a matrix b, if you are using fractions (such as is the case for the Pascal matrices Px=b), you must add a period to the entries to cast them as floating point numbers. IF YOU DO NOT, THE PROGRAM WILL NOT OUTPUT THE CORRECT X.
	Ex: b = matrix([1], [1./2.], [1./3.], [1./4.], ..., )

qr_fact_househ(matrix)
	- Input: square numpy matrix
	- Output: an array of resulting orthogonal matrix Q, upper-triangular matrix R, and error of factorization from use of Householder Reflection matrices (Q -> array[0] ; R -> array[1] ; error -> array[2])

functions from part 1d
	- TODO




