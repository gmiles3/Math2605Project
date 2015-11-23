import numpy as np


def matrixMult(A, B):
    a_rows = len(A)
    b_cols = len(B[0])
    b_len = len(B);

    new = np.zeros([a_rows, b_cols], dtype=int)

    for x in range(a_rows):
        for y in range(b_cols):
            for z in range(b_len):
                new[x][y] += A[x][z] * B[z][y]

    return new


# test cases

def main():
    arr1 = np.array([[1, 2], [2, 1], [3, 2]])
    arr2 = np.array([[3, 4],
                     [4, 3]])

    answer1 = np.array([[11, 10],
                        [10, 11],
                        [17, 18]])

    print("matrix multiplication answer is:", matrixMult(arr1, arr2))
    print("actual answer should be: ", answer1)


main()
