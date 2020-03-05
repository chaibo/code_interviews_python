"""
题目：0, 1, ..., n-1 这 n 个数字排成一个圆圈，从数字 0 开始，每次从这个圆圈里删除第
m 个数字。求出这个圆圈里剩下的最后一个数字。
"""


def last_remain(n, m):
    if (n < 1) or (m < 1):
        return -1

    last = 0
    for i in range(2, n + 1):
        last = (last + m) % i

    return last


def test():
    print("n = {}, m = {}, last = {}".format(0, 3, last_remain(0, 3)))
    print("n = {}, m = {}, last = {}".format(5, 3, last_remain(5, 3)))
    print("n = {}, m = {}, last = {}".format(6, 2, last_remain(6, 2)))
    print("n = {}, m = {}, last = {}".format(6, 6, last_remain(6, 6)))
    print("n = {}, m = {}, last = {}".format(6, 7, last_remain(6, 7)))
    print("n = {}, m = {}, last = {}".format(6, 0, last_remain(6, 0)))
    print("n = {}, m = {}, last = {}".format(10000, 99, last_remain(10000, 99)))


if __name__ == '__main__':
    test()
