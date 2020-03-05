"""
题目：假设把某股票的价格照时间先后顺序存储在数组中，请问买卖该股票一次可能获得的最大利润是多少？
例如，一只股票在某些时间节点的价格为 {9, 11, 8, 5, 7, 12, 16, 14}。如果我们能在价格为 5
的时候买入并在价格为 16 时卖出，则能收获最大的利润 11。
"""


def max_diff(numbers):
    if (not numbers) or (len(numbers) < 2):
        return 0

    length = len(numbers)
    min_num = numbers[0]
    max_diff = numbers[1] - min_num

    for i in range(2, length):
        if numbers[i - 1] < min_num:
            min_num = numbers[i - 1]

        current_diff = numbers[i] - min_num

        if current_diff > max_diff:
            max_diff = current_diff

    return max_diff


def test():
    arr1 = None
    arr2 = []
    arr3 = [4]
    arr4 = [3, 7]
    arr5 = [7, 3]
    arr6 = [1, 2, 3, 4, 5]
    arr7 = [7, 6, 5, 4, 3, 2, 1]
    arr8 = [9, 11, 8, 5, 7, 12, 16, 14]

    print("数组: {}, 最大值: {}".format(arr1, max_diff(arr1)))
    print("数组: {}, 最大值: {}".format(arr2, max_diff(arr2)))
    print("数组: {}, 最大值: {}".format(arr3, max_diff(arr3)))
    print("数组: {}, 最大值: {}".format(arr4, max_diff(arr4)))
    print("数组: {}, 最大值: {}".format(arr5, max_diff(arr5)))
    print("数组: {}, 最大值: {}".format(arr6, max_diff(arr6)))
    print("数组: {}, 最大值: {}".format(arr7, max_diff(arr7)))
    print("数组: {}, 最大值: {}".format(arr8, max_diff(arr8)))


if __name__ == '__main__':
    test()
