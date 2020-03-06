"""
题目：写一个函数，求两个整数之和，要求在函数体内不得使用 "+"、"-"、"x"、"/" 四则运算符号。
"""

"""
Python 位数是动态的，所以该方法在Python中对部分负数情况不适用，只在介绍思想。
"""


def add(num1, num2):
    while num2:
        s = num1 ^ num2
        carry = (num1 & num2) << 1

        num1 = s
        num2 = carry

    return num1


def test():
    print("{} + {} = {}".format(0, 0, add(0, 0)))
    print("{} + {} = {}".format(1, 0, add(1, 0)))
    print("{} + {} = {}".format(0, 1, add(0, 1)))
    print("{} + {} = {}".format(4, 5, add(4, 5)))
    print("{} + {} = {}".format(78, 89, add(78, 89)))


if __name__ == "__main__":
    test()

