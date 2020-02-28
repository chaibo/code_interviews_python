"""
题目：输入数字 n，按顺序打印出从 1 到最大的 n 位十进制数。
比如输入3，则打印出1、2、3一直到最大的 3 位数 999。
"""

def print_1_to_max_n_digits1(n):
    if n <= 0:
        return

    number = [0] * n

    while not increment(number, n):
        print_number(number, n)


def increment(number, n):
    is_over_flow = False  # 是否溢出
    take_over = 0   # 进位

    for i in range(n - 1, -1, -1):
        n_sum = number[i] + take_over

        if i == n-1:
            n_sum += 1

        if n_sum >= 10:
            if i == 0:
                is_over_flow = True
            else:
                n_sum = 10 - n_sum
                take_over = 1
                number[i] = n_sum
        else:
            number[i] = n_sum
            break

    return is_over_flow


def print_number(number, n):
    is_beginning_0 = True
    for i in range(n):

        if is_beginning_0 and number[i] != 0:
            is_beginning_0 = False

        if not is_beginning_0:
            print(number[i], end='')

    print()

print_1_to_max_n_digits1(-1)
print_1_to_max_n_digits1(0)
print_1_to_max_n_digits1(1)
print_1_to_max_n_digits1(2)
print_1_to_max_n_digits1(3)


"""
递归解法
"""
def print_1_to_max_n_digits2(n):
    if n <= 0:
        return

    number = [0] * n

    for i in range(10):
        number[0] = i
        print_1_to_max_n_digits_r(number, n, 0)

def print_1_to_max_n_digits_r(number, length, index):
    if index == length - 1:
        print_number(number, length)
        return

    for i in range(10):
        number[index + 1] = i
        print_1_to_max_n_digits_r(number, length, index + 1)


print_1_to_max_n_digits2(-1)
print_1_to_max_n_digits2(0)
print_1_to_max_n_digits2(1)
print_1_to_max_n_digits2(2)
print_1_to_max_n_digits2(3)
