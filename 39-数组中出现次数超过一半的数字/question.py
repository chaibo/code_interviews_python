"""
题目：数组中有一个数字出现的次数超过数组长度的一半，请找出这个数字。
例如，输入一个长度为 9 的数组 {1, 2, 3, 2, 2, 2, 5, 4, 2}。
由于数字2在数组中出现了 5 次，超过数组长度的一半，因此输出 2。
"""


def more_than_half_num1(numbers):
    if not numbers:
        return False, 0

    length = len(numbers)
    middle = length >> 1
    start = 0
    end = length - 1

    index = partition(numbers, start, end)
    while index != middle:
        if index > middle:
            end = index - 1
            index = partition(numbers, start, end)
        else:
            start = index + 1
            index = partition(numbers, start, end)

    result = numbers[middle]

    if not check_more_than_half(numbers, result):
        return False, 0

    return True, result


def partition(array, low, high):
    pivot_value = array[low]

    while low < high:
        while (low < high) and (array[high] >= pivot_value):
            high -= 1
        array[low] = array[high]
        while (low < high) and (array[low] <= pivot_value):
            low += 1
        array[high] = array[low]

    array[low] = pivot_value
    return low


def check_more_than_half(numbers, number):
    times = 0
    length = len(numbers)
    for i in range(length):
        if numbers[i] == number:
            times += 1

    is_more_than_half = True
    if times * 2 <= length:
        is_more_than_half = False

    return is_more_than_half


# 解法二
def more_than_half_num2(numbers):
    if not numbers:
        return False, 0

    result = numbers[0]
    times = 1
    for i in range(1, len(numbers)):
        if times == 0:
            result = numbers[i]
            times = 1
        elif numbers[i] == result:
            times += 1
        else:
            times -= 1

    if not check_more_than_half(numbers, result):
        return False, 0

    return True, result


def test():
    test_case1 = None
    test_case2 = []
    test_case3 = [1]
    test_case4 = [1, 2, 3, 2, 2, 2, 5, 4, 2]
    test_case5 = [1, 2, 3, 2, 2, 5, 4, 2, 6]
    test_case6 = [1, 2, 3, 2, 2, 2, 4, 6]
    test_case7 = [1, 2, 3, 2, 2, 5, 4, 6]

    print("测试解法二: ")
    print("测试用例: ", test_case1)
    print("结果: ", more_than_half_num2(test_case1))
    print("测试用例: ", test_case2)
    print("结果: ", more_than_half_num2(test_case2))
    print("测试用例: ", test_case3)
    print("结果: ", more_than_half_num2(test_case3))
    print("测试用例: ", test_case4)
    print("结果: ", more_than_half_num2(test_case4))
    print("测试用例: ", test_case5)
    print("结果: ", more_than_half_num2(test_case5))
    print("测试用例: ", test_case6)
    print("结果: ", more_than_half_num2(test_case6))
    print("测试用例: ", test_case7)
    print("结果: ", more_than_half_num2(test_case7))

    print("测试解法一: ")
    print("测试用例: ", test_case1)
    print("结果: ", more_than_half_num1(test_case1))
    print("测试用例: ", test_case2)
    print("结果: ", more_than_half_num1(test_case2))
    print("测试用例: ", test_case3)
    print("结果: ", more_than_half_num1(test_case3))
    print("测试用例: ", test_case4)
    print("结果: ", more_than_half_num1(test_case4))
    print("测试用例: ", test_case5)
    print("结果: ", more_than_half_num1(test_case5))
    print("测试用例: ", test_case6)
    print("结果: ", more_than_half_num1(test_case6))
    print("测试用例: ", test_case7)
    print("结果: ", more_than_half_num1(test_case7))


if __name__ == '__main__':
    test()
