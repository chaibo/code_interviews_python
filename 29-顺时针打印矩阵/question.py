"""
题目：输入一个矩阵，按照从外向里以顺时针的顺序依次打印出每一个数字。
例如，如果输入如下矩阵：
1   2   3   4
5   6   7   8
9   10  11  12
13  14  15  16
则依次打印出数字 1, 2, 3, 4, 8, 12, 16, 15, 14, 13, 9, 5, 6, 7, 11, 10
"""

def print_matrix_clockwisely(matrix, rows , cols):
    if (matrix is None) or (rows <= 0) or (cols <= 0):
        return

    start = 0

    while (cols > start * 2) and (rows > start * 2):
        print_matrix_in_circle(matrix, rows, cols, start)
        start += 1

    print()


def print_matrix_in_circle(matrix, rows, cols, start):
    end_row = rows - 1 - start
    end_col = cols - 1 - start

    # 从左往右打印一行
    for i in range(start, end_col + 1):
        print(matrix[start][i], end=' ')

    # 从上往下打印一列
    if start < end_row:
        for i in range(start + 1, end_row + 1):
            print(matrix[i][end_col], end=' ')

    # 从右往左打印一行
    if (start < end_row) and (start < end_col):
        for i in range(end_col - 1, start - 1, -1):
            print(matrix[end_row][i], end=' ')

    # 从下到上打印一列
    if (start < end_col) and (start < end_row - 1):
        for i in range(end_row - 1, start, -1):
            print(matrix[i][start], end=' ')


matrix1 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]
print_matrix_clockwisely(matrix1, 4, 4)

matrix2 = [[1, 2, 3, 4]]
print_matrix_clockwisely(matrix2, 1, 4)

matrix3 = [[1], [2], [3], [4]]
print_matrix_clockwisely(matrix3, 4, 1)

matrix4 = [[1]]
print_matrix_clockwisely(matrix4, 1, 1)

matrix5 = [[1, 2, 3, 4], [5, 6, 7, 8]]
print_matrix_clockwisely(matrix5, 2, 4)

matrix6 = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12]]
print_matrix_clockwisely(matrix6, 3, 4)
