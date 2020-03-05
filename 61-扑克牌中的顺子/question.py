"""
题目：从扑克牌中随机抽 5 张牌，判断是不是一个顺子，即这 5 张牌是不是连续的。
2 ~ 10 为数字本身，A 为 1， J 为 11，Q 为 12，K 为 13，而大、小王可以看成任意数字。
"""


def is_con(numbers):
    if (not numbers) or (len(numbers) < 1):
        return False

    length = len(numbers)

    numbers.sort()

    num_of_zero = 0
    num_of_gap = 0

    for num in numbers:
        if num == 0:
            num_of_zero += 1

    small = num_of_zero
    big = small + 1

    while big < length:
        if numbers[small] == numbers[big]:
            return False

        num_of_gap += numbers[big] - numbers[small] - 1
        small = big
        big += 1

    return num_of_zero >= num_of_gap


def test():
    num1 = None
    num2 = []
    num3 = [3, 1, 4, 0, 0]
    num4 = [3, 1, 4, 6, 0]
    num5 = [3, 2, 1, 4, 5]
    num6 = [3, 6, 7, 7, 8]
    num7 = [3, 4, 5, 6, 8]

    print("{} 是否是顺子: ".format(num1), end='')
    print(is_con(num1))

    print("{} 是否是顺子: ".format(num2), end='')
    print(is_con(num2))

    print("{} 是否是顺子: ".format(num3), end='')
    print(is_con(num3))

    print("{} 是否是顺子: ".format(num4), end='')
    print(is_con(num4))

    print("{} 是否是顺子: ".format(num5), end='')
    print(is_con(num5))

    print("{} 是否是顺子: ".format(num6), end='')
    print(is_con(num6))

    print("{} 是否是顺子: ".format(num7), end='')
    print(is_con(num7))


if __name__ == '__main__':
    test()
