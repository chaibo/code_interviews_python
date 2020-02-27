"""
题目：青蛙跳台阶问题
一只青蛙一次可以跳上 1 级台阶，也可以跳上 2 级台阶。求该青蛙跳上一个 n 级的台阶总共有多少种跳法。
打印走法。
"""

"""
f(1) = 1
f(2) = 2
f(n) = f(n-1) + f(n-2)  n>2
"""

def step_count(n):
    if n <= 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2

    step1 = 1
    step2 = 2

    step_n = 0
    for i in range(3, n+1):
        step_n = step1 + step2
        step1 = step2
        step2 = step_n

    return step_n

def print_step(pre_step, left_step):
    """
    :param pre_step: 代表之前的步数
    :param left_step:
    :return:
    """

    if pre_step is None:
        pre_step = ""

    if left_step <= 0:
        print(pre_step)
        return

    if left_step == 1:
        print(pre_step + "1")
        return

    for i in [1, 2]:
        print_step(pre_step + str(i) + " ", left_step-i)


print(step_count(10))
print("走法：")
print_step(None, 10)
