"""
题目：数字一012345678910111213141516...的格式序列化到一个字符数列中。
在这个序列中，第 5 位 (从 0 开始计数) 是 5， 第 13 位是 1，第 19 位是 4， 等等。
请写一个函数，求任意第 n 位对应的数字。
"""


def digit_at_index(index):
    if index < 0:
        return -1

    digits = 1

    while True:
        numbers = count_of_integer(digits)
        if index < numbers * digits:
            return find_digit(index, digits)

        index -= digits * numbers
        digits += 1

    return -1


def count_of_integer(digits):
    """
    求 digits 位的数字个数。
    """

    if digits == 1:
        return 10

    return 9 * pow(10, digits - 1)


def find_digit(index, digits):
    number = begin_number(digits) + index // digits
    index_from_right = digits - index % digits
    for i in range(1, index_from_right):
        number = number // 10

    return number % 10


def begin_number(digits):
    """
    求 digits 位数的第一个数。
    """

    if digits == 1:
        return 0

    return pow(10, digits - 1)


def test():
    test_case1 = 0
    test_case2 = 1
    test_case3 = 5
    test_case4 = 10
    test_case5 = 13
    test_case6 = 19
    test_case7 = 190
    test_case8 = 1000

    print("index {} is {}.".format(test_case1, digit_at_index(test_case1)))
    print("index {} is {}.".format(test_case2, digit_at_index(test_case2)))
    print("index {} is {}.".format(test_case3, digit_at_index(test_case3)))
    print("index {} is {}.".format(test_case4, digit_at_index(test_case4)))
    print("index {} is {}.".format(test_case5, digit_at_index(test_case5)))
    print("index {} is {}.".format(test_case6, digit_at_index(test_case6)))
    print("index {} is {}.".format(test_case7, digit_at_index(test_case7)))
    print("index {} is {}.".format(test_case8, digit_at_index(test_case8)))


if __name__ == '__main__':
    test()
