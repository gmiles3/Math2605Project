from numpy import *

# GIVENS ROTATION

# Calculates Givens rotation
#
# @param matA the matrix to be factored
# @return returns a list with the Q and R matrix and the error
def qr_fact_givens(matA):
    pivRow = 0
    rotList = []
    invRotList = []
    givensRotAnswer = []
    rMat = matA
    qMat = 1
    # iterating over the columns
    for i in range(0,matA.shape[1] - 1):
        # iterating over the rows
        for j in range(0, matA.shape[0] - 1):
            x = matA[pivRow, i]
            y = matA[pivRow + 1, i]
            targetR = pivRow + 1
            targetC = i
            givMat = buildRotMat(matA.shape[0], targetR, targetC, matA[pivRow,i],matA[targetR,targetC])
            rotList.append(givMat)

            invRotList.append(givensInverse(givMat,targetR, targetC))

        pivRow += 1
    for m in rotList:
        #Call Matrix Multiplier
        rMat = dot(rMat, m)

    invRotList.reverse()
    for n in invRotList:
        #Call Matrix Multiplier
        qMat = dot(qMat, n)
        #Call Matrix Multiplier
    error = dot(qMat,rMat) - matA
    givensRotAnswer.append(rMat)
    givensRotAnswer.append(qMat)
    givensRotAnswer.append(error)
    return givensRotAnswer




# Helper method that builds the rotation matrices
#
# @size the number of rows/col of the matrix
# @return returns the rotational givens matrix
def buildRotMat(size,tRow, tCol, x, y):
    #import pdb; pdb.set_trace()
    cs = x / (sqrt(pow(x,2) + pow(y,2)))
    sn = -y / (sqrt(pow(x,2) + pow(y,2)))
    rotMat = identity(size)
    rotMat[tRow,tRow] = cs
    rotMat[tRow,tCol] = sn
    rotMat[tCol,tRow] = -sn
    rotMat[tCol,tCol] = cs
    return rotMat


# Calculates the inverse of the rotation matrix
#
# @param gMat the current givens rotation matrix
# @param tRow the targets row
# @param tCol the targets column
# @return returns the inverse of the current givens rotation matrix
def givensInverse(gMat, tRow, tCol):
    gMat[tRow,tCol] *= -1
    gMat[tCol,tRow] *= -1
    return gMat

##### TESTING ######

# QR FACTORIZATION
def main():

    pMatrix = matrix([[1,1,1,1],
                    [1,2,3,4],
                    [1,3,6,10],
                    [1,4,10,20]])

    bVector = matrix([[1],
                    [1/2],
                    [1/3],
                    [1,4]])

    # Givens Rotation Test Case
    QGivensAnswer = matrix([[0.5, -0.67082, 0.5, -0.223607],
                       [0.5, -0.223607, -0.5, 0.67082],
                       [0.5, 0.223607, -0.5, -0.67082],
                       [0.5, 0.67082, 0.5, 0.223607]])

    RGivensAnswer = matrix([[2, 5, 10, 17.5],
                       [0, 2.23607, 6.7082, 14.0872],
                       [0, 0, 1,3.5],
                       [0, 0, 0, 0.223607]])
    print("Givens Rotation  equality for Q is :", allclose(qr_fact_givens(pMatrix)[0], QGivensAnswer))
    print("Givens Rotation  equality for R is :", allclose(qr_fact_givens(pMatrix)[1],RGivensAnswer))
main()
