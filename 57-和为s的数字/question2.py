"""
题目：和为 s 的连续正数序列。
输入一个正数 s，打印出所有和为 s 的连续正数序列(至少含有两个数)。
例如，输入15，由于 1+2+3+4+5=4+5+6=7+8=15，所以打印出 3 个连续序列
1 ~ 5、4 ~ 6 和 7 ~ 8。
"""


def find_seq(s):
    if s < 3:
        return

    small = 1
    big = 2
    mid = (s + 1) // 2

    cur_sum = small + big

    while small < mid:
        if cur_sum == s:
            print_seq(small, big)

        while (cur_sum > s) and (small < mid):
            cur_sum -= small
            small += 1

            if cur_sum == s:
                print_seq(small, big)

        big += 1
        cur_sum += big


def print_seq(small, big):
    for i in range(small, big + 1):
        print(i, end=' ')

    print()


def test():
    print("和为 {} 的连续序列为: ".format(0))
    find_seq(0)
    print("和为 {} 的连续序列为: ".format(2))
    find_seq(2)
    print("和为 {} 的连续序列为: ".format(3))
    find_seq(3)
    print("和为 {} 的连续序列为: ".format(4))
    find_seq(4)
    print("和为 {} 的连续序列为: ".format(9))
    find_seq(9)
    print("和为 {} 的连续序列为: ".format(100))
    find_seq(100)


if __name__ == '__main__':
    test()
