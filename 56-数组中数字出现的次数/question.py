"""
题目：数组中只出现一次的两个数字。
一个整型数组里除两个数字之外，其他数字都出现了两次。请写程序找出两个只出现一次的数字。
要求时间复杂度是 O(n)，空间复杂度是 O(1)。
"""


def find_numbers_appear_once(array, nums):
    if (not array) or (len(array) < 2):
        return

    array_xor = 0
    for data in array:
        array_xor ^= data

    index_of_1 = find_first_bit_1(array_xor)

    num1 = 0
    num2 = 0

    for data in array:
        if is_bit1(data, index_of_1):
            num1 ^= data
        else:
            num2 ^= data

    nums.append(num1)
    nums.append(num2)


def find_first_bit_1(num):
    index = 0
    while num & 1 == 0:
        num = num >> 1
        index += 1

    return index


def is_bit1(num, index):
    num = num >> index
    return bool(num & 1)


def test():
    array1 = None
    result1 = []
    find_numbers_appear_once(array1, result1)

    array2 = []
    result2 = []
    find_numbers_appear_once(array2, result2)

    array3 = [1]
    result3 = []
    find_numbers_appear_once(array3, result3)

    array4 = [1, 2]
    result4 = []
    find_numbers_appear_once(array4, result4)

    array5 = [2, 4, 3, 6, 3, 2, 5, 5]
    result5 = []
    find_numbers_appear_once(array5, result5)

    print("数组 {} 中只出现一次的两个数字是 {}".format(array1, result1))
    print("数组 {} 中只出现一次的两个数字是 {}".format(array2, result2))
    print("数组 {} 中只出现一次的两个数字是 {}".format(array3, result3))
    print("数组 {} 中只出现一次的两个数字是 {}".format(array4, result4))
    print("数组 {} 中只出现一次的两个数字是 {}".format(array5, result5))


if __name__ == '__main__':
    test()
