"""
题目：输入一个含有 8 个数字的数组，判断有没有可能把这 8 个数字分别放到
正方体的 8 个顶点上，使得正方体上三组相对的面上的 4 个顶点的和都相等。
"""


def cube_vertices(array):
    if (not array) or (len(array) != 8):
        return False

    return cube_vertices_core(array, 0)


def cube_vertices_core(array, index):
    length = len(array)
    result = False
    if index == length:
        if ((array[0] + array[1] + array[2] + array[3])
            == (array[4] + array[5] + array[6] + array[7])) \
                and ((array[0] + array[2] + array[4] + array[6])
                     == (array[1] + array[3] + array[5] + array[7])) \
                and ((array[0] + array[1] + array[4] + array[5])
                     == (array[3] + array[4] + array[6] + array[7])):
            result = True
    else:
        for i in range(index, length):
            temp = array[i]
            array[i] = array[index]
            array[index] = temp

            result = cube_vertices_core(array, index + 1)

            temp = array[i]
            array[i] = array[index]
            array[index] = temp

            if result:
                break

    return result


def test():
    test_case1 = None
    test_case2 = []
    test_case3 = [1]
    test_case4 = [1, 2, 3, 4, 5, 6, 7]
    test_case5 = [1, 2, 3, 1, 2, 3, 2, 2]
    test_case6 = [1, 2, 3, 1, 8, 3, 2, 2]

    print("数组：{}，是否可能：{}".format(test_case1, cube_vertices(test_case1)))
    print("数组：{}，是否可能：{}".format(test_case2, cube_vertices(test_case2)))
    print("数组：{}，是否可能：{}".format(test_case3, cube_vertices(test_case3)))
    print("数组：{}，是否可能：{}".format(test_case4, cube_vertices(test_case4)))
    print("数组：{}，是否可能：{}".format(test_case5, cube_vertices(test_case5)))
    print("数组：{}，是否可能：{}".format(test_case6, cube_vertices(test_case6)))


if __name__ == '__main__':
    test()
