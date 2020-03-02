"""
题目：输入一个字符串，打印出该字符串中字符的所有组合。
例如，输入字符串 abc，则打印出由字符 a, b, c 所能组合出的所有字符串 a、b、c、ab、ac、
bc、abc。
"""


def combination(string):
    if not string:
        return

    result = []

    length = len(string)
    for i in range(1, length + 1):
        combination_core(string, i, result)


def combination_core(string, m, result):
    if m == 0:
        print(''.join(result))
        return

    if len(string) < m:
        return

    result.append(string[0])
    combination_core(string[1:], m - 1, result)
    result.pop()
    combination_core(string[1:], m, result)


def test():
    test_case1 = None
    test_case2 = ''
    test_case3 = 'a'
    test_case4 = 'ab'
    test_case5 = 'abc'
    test_case6 = 'abcd'

    print("字符串 {} 的组合：".format(test_case1))
    combination(test_case1)
    print("字符串 {} 的组合：".format(test_case2))
    combination(test_case2)
    print("字符串 {} 的组合：".format(test_case3))
    combination(test_case3)
    print("字符串 {} 的组合：".format(test_case4))
    combination(test_case4)
    print("字符串 {} 的组合：".format(test_case5))
    combination(test_case5)
    print("字符串 {} 的组合：".format(test_case6))
    combination(test_case6)


if __name__ == '__main__':
    test()
