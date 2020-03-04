"""
题目：数字在排序数组中出现的次数。
统计一个数字在排序数组中出现的次数。例如，输入排序数组 {1, 2, 3, 3, 3, 3, 4, 5} 和数字 3，
由于 3 在这个数组中出现了 4 次，因此输出 4。
"""


def get_first_k(array, k):
    length = len(array)
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == k:
            if (mid > 0 and array[mid - 1] != k) or (mid == 0):
                return mid
            else:
                end = mid - 1
        elif array[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def get_last_k(array, k):
    length = len(array)
    start = 0
    end = length - 1

    while start <= end:
        mid = (start + end) // 2

        if array[mid] == k:
            if (mid < length - 1 and array[mid + 1] != k) or (
                    mid == length - 1):
                return mid
            else:
                start = mid + 1
        elif array[mid] > k:
            end = mid - 1
        else:
            start = mid + 1

    return -1


def get_num_of_k(array, k):
    num = 0

    if array:
        first = get_first_k(array, k)
        last = get_last_k(array, k)

        if (first > -1) and (last > -1):
            num = last - first + 1

    return num


def test():
    array1 = None
    array2 = []
    array3 = [3]
    array4 = [1, 2, 3, 3, 3, 3, 4, 5]

    print("数组 {} 中，{} 出现了 {} 次.".format(array1, 3,
                                        get_num_of_k(array1, 3)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array2, 3,
                                        get_num_of_k(array2, 3)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array3, 3,
                                        get_num_of_k(array3, 3)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array3, 4,
                                        get_num_of_k(array3, 4)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array4, 1,
                                        get_num_of_k(array4, 1)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array4, 3,
                                        get_num_of_k(array4, 3)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array4, 5,
                                        get_num_of_k(array4, 5)))
    print("数组 {} 中，{} 出现了 {} 次.".format(array4, 3,
                                        get_num_of_k(array4, 7)))


if __name__ == '__main__':
    test()