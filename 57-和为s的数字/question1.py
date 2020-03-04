"""
题目：和为 s 的两个数字。
输入一个递增排序的数组和一个数字 s，在数组中查找两个数，使得它们的和正好是 s。
如果有多对数字的和等于 s，则输出任意一对即可。
"""


def find_numbers(array, s):
    if (not array) or (len(array) < 2):
        return None

    low = 0
    high = len(array) - 1

    result = []

    while low < high:
        cur_sum = array[low] + array[high]

        if cur_sum == s:
            result.append(array[low])
            result.append(array[high])
            break
        elif cur_sum > s:
            high -= 1
        else:
            low += 1

    return result


def test():
    array1 = None
    sum1 = 10

    array2 = []
    sum2 = 10

    array3 = [2]
    sum3 = 10

    array4 = [1, 2, 4, 7, 11, 15]
    sum4 = 15

    array5 = [1, 2, 4, 7, 11, 15]
    sum5 = 50

    print("数组 {} 中，和为 {} 的两个值是 {}".format(array1, sum1,
                                          find_numbers(array1, sum1)))
    print("数组 {} 中，和为 {} 的两个值是 {}".format(array2, sum2,
                                          find_numbers(array2, sum2)))
    print("数组 {} 中，和为 {} 的两个值是 {}".format(array3, sum3,
                                          find_numbers(array3, sum3)))
    print("数组 {} 中，和为 {} 的两个值是 {}".format(array4, sum4,
                                          find_numbers(array4, sum4)))
    print("数组 {} 中，和为 {} 的两个值是 {}".format(array5, sum5,
                                          find_numbers(array5, sum5)))


if __name__ == '__main__':
    test()
