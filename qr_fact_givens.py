from numpy import *
from matrixMult import *
from pascal_generate import *

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



