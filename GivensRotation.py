from numpy import *

def qr_fact_givens(matA):
    n = len(matA)
    rot_list = []
    for i in range(0, n):
        for j in range(i+1, n):
            if matA[j,i] != 0:
                rot_matrix = build_rot_mat(n, j, i, matA[i,i], matA[j,i])
                rot_list.append(rot_matrix)
                matA = dot(rot_matrix, matA)
    rot_list.reverse()
    qMat = rot_list[0].transpose()
    for k in range(1, len(rot_list)):
        qMat = dot(rot_list[k].transpose(), qMat)
    return (qMat, matA)

# Helper method that builds the rotation matrices
#
# @size the number of rows/col of the matrix
# @return returns the rotational givens matrix
def build_rot_mat(size,tRow, tCol, x, y):
    #import pdb; pdb.set_trace()
    cs = x / (sqrt(pow(x,2) + pow(y,2)))
    sn = -y / (sqrt(pow(x,2) + pow(y,2)))
    rotMat = identity(size)
    rotMat[tRow,tRow] = cs
    rotMat[tRow,tCol] = sn
    rotMat[tCol,tRow] = -sn
    rotMat[tCol,tCol] = cs
    return rotMat
