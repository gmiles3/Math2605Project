import numpy as np

def matrixMult(A, B):

	A_Rows = len(A)
	B_Cols = len(B[0])
	b_len = len(B);

	new = np.zeros([A_Rows, B_Cols], dtype = int)

	for x in range(A_Rows):
		for y in range(B_Cols):
			for z in range (b_len):
				new[x][y] += A[x][k] * B[k][j]
