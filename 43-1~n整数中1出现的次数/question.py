"""
题目：输入一个整数 n，求 1~n 这 n 个整数的十进制表示中 1 出现的次数。
例如：输入 12， 1~12 这些整数中包含 1 的数字有 1、10、11 和 12，1 一共出现了 5 次。
"""


def num_of_1(n):
    if n <= 0:
        return 0

    str_num = str(n)
    length = len(str_num)

    return num_of_1_recursive(str_num, length, 0)


def num_of_1_recursive(str_num, length, index):
    if index >= length:
        return 0

    first = int(str_num[index])

    if (index == length - 1) and (first == 0):
        return 0
    if (index == length - 1) and (first > 0):
        return 1

    # 最高位为 1 的数字的数目
    num_first_digit = 0
    if first > 1:
        num_first_digit += pow(10, length - index - 1)
    else:
        num_first_digit += int(str_num[index + 1:]) + 1

    num_other_digit = first * (length - index - 1) * pow(10, length - index - 2)

    num_recursive = num_of_1_recursive(str_num, length, index + 1)

    return num_first_digit + num_other_digit + num_recursive


def test():
    test_case1 = 0
    test_case2 = 1
    test_case3 = 5
    test_case4 = 10
    test_case5 = 15
    test_case6 = 55
    test_case7 = 99
    test_case8 = 10000
    test_case9 = 11345
    test_case10 = 21345

    print("输入 n = {}, 1 的数目: {}".format(test_case1, num_of_1(test_case1)))
    print("输入 n = {}, 1 的数目: {}".format(test_case2, num_of_1(test_case2)))
    print("输入 n = {}, 1 的数目: {}".format(test_case3, num_of_1(test_case3)))
    print("输入 n = {}, 1 的数目: {}".format(test_case4, num_of_1(test_case4)))
    print("输入 n = {}, 1 的数目: {}".format(test_case5, num_of_1(test_case5)))
    print("输入 n = {}, 1 的数目: {}".format(test_case6, num_of_1(test_case6)))
    print("输入 n = {}, 1 的数目: {}".format(test_case7, num_of_1(test_case7)))
    print("输入 n = {}, 1 的数目: {}".format(test_case8, num_of_1(test_case8)))
    print("输入 n = {}, 1 的数目: {}".format(test_case9, num_of_1(test_case9)))
    print("输入 n = {}, 1 的数目: {}".format(test_case10, num_of_1(test_case10)))


if __name__ == '__main__':
    test()
