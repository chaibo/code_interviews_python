"""
题目：把 n 个骰子扔在地上，所有骰子朝上一面的点数之和为 s。
输入 n，打印出 s 的所有可能的值出现的概率。
"""

MAX_VALUE = 6

"""
解法一：基于递归
"""


def print_prob1(n):
    if n < 1:
        return

    max_sum = MAX_VALUE * n
    prob_l = [0] * (max_sum - n + 1)

    for i in range(1, MAX_VALUE + 1):
        prob(n, n, i, prob_l)

    total = pow(MAX_VALUE, n)

    for i in range(n, max_sum + 1):
        ratio = float(prob_l[i - n] / total)
        print("{} : {}".format(i, ratio))


def prob(n, current, sum, prob_l):
    if current == 1:
        prob_l[sum - n] += 1
    else:
        for i in range(1, MAX_VALUE + 1):
            prob(n, current - 1, sum + i, prob_l)


"""
解法二：基于循环。
f(n) = f(n-1) + f(n-2) + f(n-3) + f(n-4) + f(n-5) + f(n-6)
"""


def print_prob2(n):
    if n < 1:
        return

    max_sum = MAX_VALUE * n
    prob_l1 = [0] * (max_sum + 1)
    prob_l2 = [0] * (max_sum + 1)
    prob_l = [prob_l1, prob_l2]

    flag = 0

    for i in range(1, MAX_VALUE + 1):
        prob_l[flag][i] = 1

    for i in range(2, n + 1):
        for j in range(i):
            prob_l[1 - flag][j] = 0

        for k in range(i, MAX_VALUE * i + 1):
            prob_l[1 - flag][k] = 0
            for j in range(1, MAX_VALUE + 1):
                if j > k:
                    break
                prob_l[1 - flag][k] += prob_l[flag][k - j]

        flag = 1 - flag

    total = pow(MAX_VALUE, n)

    for i in range(n, max_sum + 1):
        ratio = float(prob_l[flag][i] / total)
        print("{} : {}".format(i, ratio))


def test():
    print("0个骰子所有值的概率: ")
    print("递归:")
    print_prob1(0)
    print("循环")
    print_prob2(0)

    print("1个骰子所有值的概率: ")
    print("递归:")
    print_prob1(1)
    print("循环")
    print_prob2(1)

    print("2个骰子所有值的概率: ")
    print("递归:")
    print_prob1(2)
    print("循环")
    print_prob2(2)

    print("3个骰子所有值的概率: ")
    print("递归:")
    print_prob1(3)
    print("循环")
    print_prob2(3)

    print("4个骰子所有值的概率: ")
    print("递归:")
    print_prob1(4)
    print("循环")
    print_prob2(4)

    print("10个骰子所有值的概率: ")
    print("递归:")
    print_prob1(10)
    print("循环")
    print_prob2(10)


if __name__ == "__main__":
    test()
