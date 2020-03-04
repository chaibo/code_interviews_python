"""
题目：0 ~ n-1 中缺失的数字。
一个长度为 n-1 的递增排序数组中的所有数字都是唯一的，并且每个数字都在范围 0 ~ n-1 之内。
在范围 0 ~ n-1 内的 n 个数字中有且只有一个数字不在该数组中，请找出这个数字。
"""


def get_missing_num(array):
    if not array:
        return -1

    length = len(array)
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] != mid:
            if (mid == 0) or (array[mid - 1] == mid - 1):
                return mid
            else:
                end = mid - 1
        else:
            start = mid + 1

    if start == length:
        return length


def test():
    array1 = None
    array2 = []
    array3 = [0]
    array4 = [1]
    array5 = [0, 1, 2, 4, 5, 6]
    array6 = [1, 2, 3, 4, 5, 6]
    array7 = [0, 1, 2, 3, 4, 5]

    print("数组 {} 缺少数组 {}.".format(array1, get_missing_num(array1)))
    print("数组 {} 缺少数组 {}.".format(array2, get_missing_num(array2)))
    print("数组 {} 缺少数组 {}.".format(array3, get_missing_num(array3)))
    print("数组 {} 缺少数组 {}.".format(array4, get_missing_num(array4)))
    print("数组 {} 缺少数组 {}.".format(array5, get_missing_num(array5)))
    print("数组 {} 缺少数组 {}.".format(array6, get_missing_num(array6)))
    print("数组 {} 缺少数组 {}.".format(array7, get_missing_num(array7)))


if __name__ == '__main__':
    test()
