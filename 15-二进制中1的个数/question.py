"""
题目：请实现一个函数，输入一个整数，输出该数二进制表示中 1 的个数。
例如，把 9 表示成二进制是 1001，有 2 位是 1。因此，如果输入 9 ，
则该函数输出 2。
"""

"""
把一个整数减去 1 之后再和原来的整数做位与运算，得到的结果
相当于把整数的二进制表示中最右边的 1 变成 0。
"""
"""
Python 中，整数位数是变长的，所以该解法不适用与负数
"""
def num_of_1(number):
    count = 0

    while number:
        count += 1
        number = number & (number - 1)

    return count


print(num_of_1(1))
print(num_of_1(0))
print(num_of_1(24434))
