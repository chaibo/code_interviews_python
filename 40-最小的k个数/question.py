"""
题目：输入 n 个整数，找出其中最小的 k 个数。
例如，输入 4、5、1、6、2、7、3、8 这 8 个数字，则最小的 4 个数字是 1、2、3、4。
"""


def least_numbers(numbers, k):
    if (not numbers) or (k > len(numbers)) or (k <= 0):
        return None

    start = 0
    end = len(numbers) - 1
    index = partition(numbers, start, end)
    while index != k - 1:
        if index > k - 1:
            end = index - 1
            index = partition(numbers, start, end)
        else:
            start = index + 1
            index = partition(numbers, start, end)

    return numbers[:k]


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


def test():
    test_case1 = None
    test_case2 = []
    test_case3 = [4, 5, 1, 6, 2, 7, 3, 8]
    test_case4 = [3, 5, 7, 9, 2, 2, 1, 4]

    print("测试数组: {}, k 值: {}".format(test_case1, 1))
    print("输出: {}".format(least_numbers(test_case1, 1)))

    print("测试数组: {}, k 值: {}".format(test_case2, 1))
    print("输出: {}".format(least_numbers(test_case2, 1)))

    print("测试数组: {}, k 值: {}".format(test_case3, 0))
    print("输出: {}".format(least_numbers(test_case3, 0)))

    print("测试数组: {}, k 值: {}".format(test_case3, 1))
    print("输出: {}".format(least_numbers(test_case3, 1)))

    print("测试数组: {}, k 值: {}".format(test_case3, 8))
    print("输出: {}".format(least_numbers(test_case3, 8)))

    print("测试数组: {}, k 值: {}".format(test_case3, 4))
    print("输出: {}".format(least_numbers(test_case3, 4)))

    print("测试数组: {}, k 值: {}".format(test_case4, 3))
    print("输出: {}".format(least_numbers(test_case4, 3)))


if __name__ == '__main__':
    test()
