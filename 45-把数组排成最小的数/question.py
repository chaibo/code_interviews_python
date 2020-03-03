"""
题目：输入一个正整数数组，把数组里所有的数字拼接起来排成一个数，打印能拼接出的所有数字中最小的一个。
例如，输入数组 {3， 32， 321}，则打印出这 3 个数字能排成的最小数字 321323。
"""

import functools


def print_min_number(array):
    if not array:
        return

    str_array = [str(x) for x in array]

    str_array.sort(key=functools.cmp_to_key(compare_func))

    return ''.join(str_array)


def compare_func(str_num1, str_num2):
    """
    两个数字 m、n 拼接成数字 mn 和 nm，若 mn < nm，则 m < n。
    """

    num1 = str_num1 + str_num2
    num2 = str_num2 + str_num1

    return (num1 > num2) - (num2 > num1)


def test():
    array1 = None
    array2 = []
    array3 = [5]
    array4 = [3, 32, 321]
    array5 = [5, 3, 2, 1, 1, 3]

    print("数组 {} 排成的最小数字: {}".format(array1, print_min_number(array1)))
    print("数组 {} 排成的最小数字: {}".format(array2, print_min_number(array2)))
    print("数组 {} 排成的最小数字: {}".format(array3, print_min_number(array3)))
    print("数组 {} 排成的最小数字: {}".format(array4, print_min_number(array4)))
    print("数组 {} 排成的最小数字: {}".format(array5, print_min_number(array5)))


if __name__ == '__main__':
    test()
