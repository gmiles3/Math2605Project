def matrixMult(A, B):
    A_Rows = A.shape[0]
    B_Cols = B.shape[1]
    if (A.shape[1] == B.shape[0]):
        newMat = zeros([A_Rows, B_Cols], dtype = float)
        for i in range(0,B_Cols):
            vecB = B[0:, i:i + 1]
            for j in range(0,A_Rows):
                vecA = A[j:j+1, 0:]
                newMat[j,i] = dot(vecA, vecB)
        return newMat
