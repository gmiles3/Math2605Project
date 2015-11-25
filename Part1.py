from numpy import *
import numpy as np

#TODO: add functions for part 1d

def lu_fact(matA):
    original = matA.copy()
    n = len(matA)                 # n is # of rows and cols
    i_matA = identity(n, float)       # i_matA will be transformed into L via all row operations that create U
    for col in range(0, n):         # for each col
        i = 0                       # initialize i
        for i in range(col, n):     # for each row
            if matA[i,col] != 0: # find pivot
                break
        if matA[i,col] != 0:
            for k in range(col + 1, n):     # for each entry beneath pivot
                if matA[k,col] != 0:     # if entry not already 0
                    multiple = matA[k,col] / matA[i,col]  # find multiple for eliminating entry
                    i_matA[k,col] = multiple # set corresponding i_matA entry to construct L
                    for c in range(0, n):   # for each entry along row, we want to apply same operation
                        matA[k,c] = matA[k,c] - (matA[i,c] * multiple)     # eliminate entry by multiplying pivot by multiple and subtracting
    derived_A = matrixMult(i_matA, matA)        # begin error calculation, compute L*U
    derived_A = derived_A - original            # compute LU - A
    current_max = 0                             # find norm by finding largest abs val of entries
    for col in range (0, n):                    # for each col
        for row in range(0, n):                 # for each row
            if abs(derived_A[row,col]) > current_max:       # if current abs val entry is bigger than max
                current_max = abs(derived_A[row, col])      # update
    return [i_matA, matA, current_max]       # return L, U, and error

def pascal_generate(n):
    matrix = np.zeros((n, n), float)       # start with square matrix of 0's
    for i in range(1, n + 1):       # for each row
        for j in range(1, n + 1):   # for each col
            matrix[i - 1,j - 1] = factorial((i - 1) + (j - 1)) / (factorial(i - 1) * factorial(j - 1))     # use provided formula for calculating entry value
    b = np.zeros((n, 1), float)            # start with b matrix of 0's
    for i in range(0, n):           # for each row in b
        b[i,0] = 1. / (i + 1)       # calculate b entry
    return [matrix, b]              # return P and b


def factorial(num):
    toReturn = 1;                   # start with 1
    while num > 0:                  # while num is greater than 0, we keep multiplying
        toReturn = toReturn * num   # multiple by number
        num = num - 1               # decrement number
    return toReturn                 # return num!

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

def qr_fact_givens(matA):
    original = matA.copy()
    n = len(matA)                   # n is # of cols and rows
    rot_list = []                   # keep track of all rotation matrices for calculation of Q
    temp = zeros(n)                 # weird error happens if I don't do this
    matA = temp + matA              # weird error happens if I don't do this
    for i in range(0, n):           # for each col
        for j in range(i+1, n):     # for each row
            if matA[j,i] != 0:      # if entry not already 0
                rot_matrix = build_rot_mat(n, j, i, matA[i,i], matA[j,i])   # build rotation matrix using pivot and target entry
                rot_list.append(rot_matrix)             # add rotation matrix to list
                matA = matrixMult(rot_matrix, matA)     # update matrix to approach R
    rot_list.reverse()                                      # reverse order of rotation matrices for multiplication
    qMat = rot_list[0].transpose()                          # transpose first rotation matrix
    for k in range(1, len(rot_list)):                       # for each rotation matrix
        qMat = matrixMult(rot_list[k].transpose(), qMat)    # multiply every rotation matrix transposed together

    derived_A = matrixMult(qMat, matA)        # begin error calculation, compute Q*R
    derived_A = derived_A - original            # compute QR - A
    current_max = 0                             # find norm by finding largest abs val of entries
    for col in range (0, n):                    # for each col
        for row in range(0, n):                 # for each row
            if abs(derived_A[row,col]) > current_max:       # if current abs val entry is bigger than max
                current_max = abs(derived_A[row, col])      # update
    return [qMat, matA, current_max]    # return Q and R

def build_rot_mat(size,tRow, tCol, x, y):
    #import pdb; pdb.set_trace()
    cs = x / sqrt(x**2 + y**2)      # cosine
    sn = -y / sqrt(x**2 + y**2)     # sine
    rotMat = identity(size)         # create identity matrix to build rotation matrix
    rotMat[tRow,tRow] = cs          # add cosine to rotation matrix
    rotMat[tRow,tCol] = sn          # add sine to rotation matrix
    rotMat[tCol,tRow] = -sn         # add -sine to rotation matrix
    rotMat[tCol,tCol] = cs          # add cosine to rotation matrix
    return rotMat

def solve_lu_b(L, U, b):
    n = len(L)                                  # N is # of rows and cols
    y = zeros((n,1), float)                     # create vector of 0's to initialize y
    x = zeros((n,1), float)                     # create vector of 0's to initialize x
    for i in range(0, n):                       # for each row (each equation in system)
        subsum = 0                              # initialize sum to 0
        for k in range(0, i):                   # part of formula for forward substitution
            subsum += (L[i,k]*y[k,0])           # part of formula for forward substitution
        y[i,0] = (1/L[i,i])*(b[i,0] - subsum)   # part of formula for forward substitution
    for i in range(n-1, -1, -1):                # for each row (each equation in system) going backwards
        subsum = 0                              # initialize sum to 0
        for k in range(i+1, n):                 # part of formula for backward substitution
            subsum += (U[i,k]*x[k,0])           # part of formula for backward substitution
        x[i,0] = (1/U[i,i])*(y[i,0] - subsum)   # part of formula for backward substitution
    return x

def solve_qr_b(Q, R, b):
    n = len(Q)                                  # N is # of rows and cols
    y = zeros((n,1), float)                     # create vector of 0's to initialize y
    x = zeros((n,1), float)                     # create vector of 0's to initialize x
    y = matrixMult(Q.transpose(), b)            # y = Qt*b
    for i in range(n-1, -1, -1):                # for each row (each equation in system) going backwards
        subsum = 0                              # initialize sum to 0
        for k in range(i+1, n):                 # part of formula for backward substitution
            subsum += (R[i,k]*x[k,0])           # part of formula for backward substitution
        x[i,0] = (1/R[i,i])*(y[i,0] - subsum)   # part of formula for backward substitution
    return x

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