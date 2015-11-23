from numpy import *

def qr_fact_givens(matA):
    n = len(matA)
    rot_list = []
    temp = zeros(n)
    matA = temp + matA
    for i in range(0, n):
        for j in range(i+1, n):
            if matA[j,i] != 0:
                rot_matrix = build_rot_mat(n, j, i, matA[i,i], matA[j,i])
                rot_list.append(rot_matrix)
                matA = matrixMult(rot_matrix, matA)
    rot_list.reverse()
    qMat = rot_list[0].transpose()
    for k in range(1, len(rot_list)):
        qMat = matrixMult(rot_list[k].transpose(), qMat)
    return (qMat, matA)

def build_rot_mat(size,tRow, tCol, x, y):
    #import pdb; pdb.set_trace()
    cs = x / sqrt(x**2 + y**2)
    sn = -y / sqrt(x**2 + y**2)
    rotMat = identity(size)
    print(cs)
    rotMat[tRow,tRow] = cs
    rotMat[tRow,tCol] = sn
    rotMat[tCol,tRow] = -sn
    rotMat[tCol,tCol] = cs
    return rotMat

