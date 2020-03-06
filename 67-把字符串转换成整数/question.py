"""
题目：实现把字符串转换为整数的功能。
"""


def str_to_int(string):
    if not string:
        return False, 0

    length = len(string)

    num = 0
    status = False

    index = 0
    minus = 1
    if string[0] == '+':
        index += 1
    elif string[0] == '-':
        minus = -1
        index += 1

    while index < length:
        if ord("0") <= ord(string[index]) <= ord("9"):
            num = num * 10 + (ord(string[index]) - ord("0"))
            index += 1
        else:
            num = 0
            break

    if index == length:
        status = True

    return status, minus * num


def test():
    print("str = {}, result = {}".format(repr(None), str_to_int(None)))
    print("str = {}, result = {}".format(repr(""), str_to_int("")))
    print("str = {}, result = {}".format(repr(" "), str_to_int(" ")))
    print("str = {}, result = {}".format(repr("+"), str_to_int("+")))
    print("str = {}, result = {}".format(repr("-"), str_to_int("-")))
    print("str = {}, result = {}".format(repr("+35345"), str_to_int("+35345")))
    print("str = {}, result = {}".format(repr("-8347"), str_to_int("-8347")))
    print("str = {}, result = {}".format(repr("647g34"), str_to_int("647g34")))


if __name__ == "__main__":
    test()
