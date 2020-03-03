"""
题目：在一个 m*n 的棋盘的每一格都放有一个礼物，每个礼物都有一定的价值 (价值大于 0)。
你可以从棋盘的左上角开始拿格子里的礼物，并每次向左或向下移动一格，直到到达棋盘的右下角。
给定一个棋盘及其上面的礼物，请计算你最多能拿到多少价值的礼物？
"""


def get_max_value(array, rows, cols):
    if (not array) or (rows <= 0) or (cols <= 0):
        return 0

    max_value = [0] * cols

    for i in range(rows):
        for j in range(cols):
            up = 0
            left = 0

            if i > 0:
                up = max_value[j]
            if j > 0:
                left = max_value[j - 1]

            max_value[j] = max(up, left) + array[i * cols + j]

    return max_value[cols - 1]


def test():
    array1 = None
    array2 = []
    array3 = [24]
    array4 = [1, 2, 3, 4]
    array5 = [3, 5, 7, 8]
    array6 = [1, 10, 3, 8, 12, 2, 9, 6, 5, 7, 4, 11, 3, 7, 16, 5]

    print("矩阵: ")
    print_matrix(array1, 0, 0)
    print("礼物最大值：{}".format(get_max_value(array1, 0, 0)))
    print("矩阵: ")
    print_matrix(array2, 0, 0)
    print("礼物最大值：{}".format(get_max_value(array2, 0, 0)))
    print("矩阵: ")
    print_matrix(array3, 1, 1)
    print("礼物最大值：{}".format(get_max_value(array3, 1, 1)))
    print("矩阵: ")
    print_matrix(array4, 1, 4)
    print("礼物最大值：{}".format(get_max_value(array4, 1, 4)))
    print("矩阵: ")
    print_matrix(array5, 4, 1)
    print("礼物最大值：{}".format(get_max_value(array5, 4, 1)))
    print("矩阵: ")
    print_matrix(array6, 4, 4)
    print("礼物最大值：{}".format(get_max_value(array6, 4, 4)))


def print_matrix(array, rows, cols):
    if not array:
        print(None)

    for i in range(rows):
        for j in range(cols):
            print(array[i * cols + j], end='   ')
        print()


if __name__ == '__main__':
    test()
