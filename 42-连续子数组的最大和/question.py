"""
题目：输入一个整形数组，数组里有正数也有负数。数组中的一个或连续多个整数组成一个子数组。
求所有子数组的和的最大值。要求时间复杂度为 O(n)。
"""


def find_greatest_sum1(array):
    if not array:
        return False, 0

    cur_sum = array[0]
    greatest_sum = array[0]
    length = len(array)

    for i in range(1, length):
        if cur_sum <= 0:
            cur_sum = array[i]
        else:
            cur_sum += array[i]

        if cur_sum > greatest_sum:
            greatest_sum = cur_sum

    return True, greatest_sum


def test():
    test_case1 = None
    test_case2 = []
    test_case3 = [1]
    test_case4 = [1, 4, 2, 3]
    test_case5 = [1, -2, 3, 10, -4, 7, 2, -5]
    test_case6 = [-5, -4, -3, -1, -2, -6]

    print("测试用例: {}, 输出: {}".format(test_case1,
                                    find_greatest_sum1(test_case1)))
    print("测试用例: {}, 输出: {}".format(test_case2,
                                    find_greatest_sum1(test_case2)))
    print("测试用例: {}, 输出: {}".format(test_case3,
                                    find_greatest_sum1(test_case3)))
    print("测试用例: {}, 输出: {}".format(test_case4,
                                    find_greatest_sum1(test_case4)))
    print("测试用例: {}, 输出: {}".format(test_case5,
                                    find_greatest_sum1(test_case5)))
    print("测试用例: {}, 输出: {}".format(test_case6,
                                    find_greatest_sum1(test_case6)))


if __name__ == '__main__':
    test()
