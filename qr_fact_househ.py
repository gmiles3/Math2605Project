# This is the house holder method
#
# @matA The matrix A
# @return Returns  A list with Q matrix, R matrix and the error
def qr_fact_househ(matA):
    daAnswer = []
    houseMatList= []
    row = matA.shape[0]
    col = matA.shape[1]
    i = 0
    j = 1
    vecV = matA[0:, 0:1]
    uNumerator = vecV.transpose() + mag(vecV) * eCal(row)
    uDenominator = mag(vecV + (mag(vecV) * eCal(row)).transpose())
    u = uNumerator / uDenominator
    hOne = matrixHN(u, col)
    houseMatList.append(hOne)
    tempMatrix = matrixMult(hOne, matA)
    for ct in range(1, col - 1):
        #row = tempMatrix.shape[0] - 1
        vecV = tempMatrix[ct : col, ct : ct + 1]
        uNumerator = vecV.transpose() + mag(vecV) * eCal(vecV.shape[0])
        uDenominator = mag(vecV.transpose() + (mag(vecV) * eCal(vecV.shape[0])))
        u = uNumerator / uDenominator
        hTilda = matrixHN(u, u.size)
        houseMat = matrixUpdate(hTilda, col, ct)
        houseMatList.append(houseMat)
        tempMatrix = matrixMult(houseMat,tempMatrix)



    #Calculate Q Matrix

    QMatrix = identity(matA.shape[0])
    RMatrix = tempMatrix


    for n in houseMatList:
        QMatrix = matrixMult(QMatrix, n)
    res = matrixMult(QMatrix, RMatrix)
    max = res[0,0]
    for i in range(0,res.shape[0]):
        for j in range(0, res.shape[1]):
            if (res[i,j] > max):
                max = res[i,j]

    error = abs(max)

    daAnswer.append(QMatrix)
    daAnswer.append(RMatrix)
    daAnswer.append(error)
    return daAnswer

# Helper method that takes the matrix
# H tilda and  places it insdide the appropriate
# identity matrix
#
# @ mat The H tilda matrix
# @ numCol The size of new matrix to be returned
# @ start The index at which to start the matrix replacement
# @ return returns HouseHolder Matrix
def matrixUpdate(mat,numCol, start):
    idMat = identity(numCol)
    start2 = start
    for i in range(start,numCol):
        for j in range(start2, numCol):
            idMat[i,j] = mat[i - start, j - start]
    return idMat

# Helper method that calculates H tilda for further iterations of HH
#
# @ uVec the u vector from H =I - 2uu^t
# @ size the size that the H tilda matrix will be
# @ return Returns H tilda
def matrixHN(uVec, size):
    idMat = identity(size)
    return idMat - 2 * matrixMult(uVec.transpose(), uVec)

# Helper method that calulates magnitude of a vector
def mag (vec):
    sum = 0

    for i in range(vec.shape[0]):
        for j in range(vec.shape[1]):
          sum += pow(vec[i,j], 2)
    return sqrt(sum)


# This method creates an e1 vector
#
# @ size the size of the e1 vector
def eCal(size):
    eVec = zeros(size)
    eVec[0] = 1
    return mat(eVec)

