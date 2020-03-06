"""
题目：求 1 + 2 + ... + n，要求不能使用乘除法，for、while、else、if、等关键字。
"""

"""
解法一：Python sum 函数。
"""


def solution1(n):
    return sum(range(1, n + 1))


"""
解法二：利用短路语句实现递归。
"""


def solution2(n):
    return n and (n + solution2(n - 1))


"""
解法三：reduce
"""
from functools import reduce


def solution3(n):
    def func(x, y):
        return x + y

    return reduce(func, list(range(0, n + 1)))


def test():
    print("n = {}, 解法一: {}, 解法二: {}, 解法三: {}"
          .format(1, solution1(1), solution2(1), solution3(1)))

    print("n = {}, 解法一: {}, 解法二: {}, 解法三: {}"
          .format(5, solution1(5), solution2(5), solution3(5)))

    print("n = {}, 解法一: {}, 解法二: {}, 解法三: {}"
          .format(10, solution1(10), solution2(10), solution3(10)))

    print("n = {}, 解法一: {}, 解法二: {}, 解法三: {}"
          .format(0, solution1(0), solution2(0), solution3(0)))


if __name__ == "__main__":
    test()
