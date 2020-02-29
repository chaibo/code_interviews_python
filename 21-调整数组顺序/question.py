"""
题目：输入一个整数数组，实现一个函数来调整该数组中数字的顺序，使得所有
奇数位于数组的前半部分，所有偶数位于数组的后半部分。
"""

def reorder(array, func = None):
    if (array is None) or (len(array)) <= 0:
        return

    if not callable(func):
        return

    low = 0
    high = len(array) - 1

    while low < high:

        while (low < high) and (not func(array[low])):
            low += 1

        while (low < high) and func(array[high]):
            high -= 1

        if low < high:
            tmp = array[low]
            array[low] = array[high]
            array[high] = tmp


def is_even(n):
    return n & 1 == 0


test_array1 = [1, 2, 3, 4, 5]
reorder(test_array1, is_even)
print(test_array1)

test_array2 = [1, 3, 5, 4, 2]
reorder(test_array2, is_even)
print(test_array2)

test_array3 = [4, 2, 3, 1, 5]
reorder(test_array3, is_even)
print(test_array3)

test_array4 = [1, 7, 3, 9, 5]
reorder(test_array4, is_even)
print(test_array4)

test_array5 = [0, 2, 6, 4, 8]
reorder(test_array5, is_even)
print(test_array5)

test_array6 = [1]
reorder(test_array6, is_even)
print(test_array6)

test_array7 = []
reorder(test_array7, is_even)
print(test_array7)

test_array8 = None
reorder(test_array8, is_even)
print(test_array8)
