"""
题目：在数组中的两个数字，如果前面一个数字大于后面的数字， 则这两个数字组成一个逆序对。
输入一个数组，求出这个数组中的逆序对的总数。例如，在数组 {7, 5, 6, 4} 中，一共存在
5 个逆序对，分别是 (7, 5)、(7, 6)、(7, 4)、(6, 4) 和 (5, 4)。
"""


def inverse_pairs(data):
    if not data:
        return 0

    copy = [x for x in data]

    return inverse_pairs_core(data, copy, 0, len(data) - 1)


def inverse_pairs_core(data, copy, start, end):
    if start == end:
        copy[start] = data[start]
        return 0

    length = (end - start) // 2

    left = inverse_pairs_core(copy, data, start, start + length)
    right = inverse_pairs_core(copy, data, start + length + 1, end)

    i = start + length
    j = end
    copy_index = end
    count = 0

    while (i >= start) and (j >= start + length + 1):
        if data[i] > data[j]:
            copy[copy_index] = data[i]
            count += (j - start - length)
            copy_index -= 1
            i -= 1
        else:
            copy[copy_index] = data[j]
            copy_index -= 1
            j -= 1

    while i >= start:
        copy[copy_index] = data[i]
        copy_index -= 1
        i -= 1

    while j >= start + length + 1:
        copy[copy_index] = data[j]
        copy_index -= 1
        j -= 1

    return left + right + count


def test():
    data1 = None
    data2 = []
    data3 = [7, 5, 6, 4]
    data4 = [1, 2, 3, 4, 5]
    data5 = [5, 4, 3, 2, 1]
    data6 = [8, 5, 6, 4, 5, 7]

    print("数组 {} 中的逆序对为: ".format(data1), end='')
    print("{} 对.".format(inverse_pairs(data1)))
    print("数组 {} 中的逆序对为: ".format(data2), end='')
    print("{} 对.".format(inverse_pairs(data2)))
    print("数组 {} 中的逆序对为: ".format(data3), end='')
    print("{} 对.".format(inverse_pairs(data3)))
    print("数组 {} 中的逆序对为: ".format(data4), end='')
    print("{} 对.".format(inverse_pairs(data4)))
    print("数组 {} 中的逆序对为: ".format(data5), end='')
    print("{} 对.".format(inverse_pairs(data5)))
    print("数组 {} 中的逆序对为: ".format(data6), end='')
    print("{} 对.".format(inverse_pairs(data6)))


if __name__ == '__main__':
    test()
