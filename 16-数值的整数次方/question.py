"""
题目：实现函数 power(base, exponent), 求 base 的 exponent 次方。
其中，base 为浮点数，exponent 为整数。
不得使用库函数，同时不需要考虑大数问题。
"""

PRECISION = 0.0000001

def power(base, exponent):

    if (abs(base - 0.0) <= PRECISION) and exponent < 0:
        raise Exception("Invalid input : 零的负数次方没有意义。")

    abs_exponent = exponent
    if exponent < 0:
        abs_exponent = - exponent

    result1 = power_with_positive_exponent1(base, abs_exponent)
    result2 = power_with_positive_exponent2(base, abs_exponent)

    if exponent < 0:
        result1 = 1.0 / result1
        result2 = 1.0 / result2

    return result1, result2


def power_with_positive_exponent1(base ,exponent):
    result = 1.0
    for i in range(exponent):
        result *= base

    return result


def power_with_positive_exponent2(base, exponent):
    if exponent == 0:
        return 1.0

    result = power_with_positive_exponent2(base, exponent >> 1)
    result *= result

    if exponent & 1 == 1:
        result *= base

    return result

print(power(1.0, 2))
print(power(1.0, 0))
print(power(1.0, -2))

print(power(3.0, 3))
print(power(3.0, 0))
print(power(3.0, -3))

print(power(-1.0, 2))
print(power(-1.0, 0))
print(power(-1.0, -2))

print(power(-3.0, 3))
print(power(-3.0, 0))
print(power(-3.0, -3))

print(power(0.0, 0))
print(power(0.0, 3))
print(power(0.0, -3))
