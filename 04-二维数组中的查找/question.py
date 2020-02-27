"""
题目：在一个二维数组中，每一行都按照从左到右递增的顺序排序，每一列都按照从上到下递增
的顺序排序。请完成一个函数，输入这样的一个二维数组和一个整数，判断数组是否含有该整数。
"""

def find(matrix, rows, columns, number):
    """
    :param matrix: 用一维数组存储的二维数组
    :param rows: 二维数组的行数
    :param columns: 二维数组的列数
    :param number: 要查找的整数
    :return: 表示是否找到的布尔值
    """

    found = False

    if (matrix is not None) and (rows > 0) and (columns > 0):

        # 从右上角开始搜索
        row = 0
        column = columns - 1

        while (row < rows) and (column >= 0):
            if matrix[row * columns + column] == number:
                found = True
                break
            elif matrix[row * columns + column] > number:
                column -= 1
            else:
                row += 1

    return found


test_case1 = [1, 2, 8, 9, 2, 4, 9, 12, 4, 7, 10, 13, 6, 8, 11, 15]
print(find(test_case1, 4, 4, 7))
print(find(test_case1, 4, 4, 1))
print(find(test_case1, 4, 4, 15))
print(find(test_case1, 4, 4, 0))
print(find(test_case1, 4, 4, 5))
print(find(test_case1, 4, 4, 16))

test_case2 = None
print(find(test_case2, 0, 0, 3))
