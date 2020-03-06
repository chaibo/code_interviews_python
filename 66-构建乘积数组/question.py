"""
题目：给定一个数组 A[0, 1, ..., n-1]，请构建一个数组 B[0, 1, ..., n-1], 其中
B中的元素 B[i] = A[0] * A[1] * ... * A[i-1] * A[i+1]* ... * A[n-1]。不能
使用除法。
"""


def multiply(array):
    if not array:
        return array

    length = len(array)
    result = [1] * length

    result[0] = 1

    for i in range(1, length):
        result[i] = result[i - 1] * array[i - 1]

    temp = 1
    for i in range(length - 2, -1, -1):
        temp *= array[i + 1]
        result[i] *= temp

    return result


def test():
    array1 = None
    array2 = []
    array3 = [4]
    array4 = [3, 5, 5, 6, 7]
    array5 = [2, 3, -5, 3, 9]
    array6 = [3, 2, 4, 0, 3]
    array7 = [4, 3, 0, 0, 3]
    array8 = [4, 0, 0, 0, 2]

    print("arr = {}, result = {}".format(array1, multiply(array1)))
    print("arr = {}, result = {}".format(array2, multiply(array2)))
    print("arr = {}, result = {}".format(array3, multiply(array3)))
    print("arr = {}, result = {}".format(array4, multiply(array4)))
    print("arr = {}, result = {}".format(array5, multiply(array5)))
    print("arr = {}, result = {}".format(array6, multiply(array6)))
    print("arr = {}, result = {}".format(array7, multiply(array7)))
    print("arr = {}, result = {}".format(array8, multiply(array8)))


if __name__ == '__main__':
    test()
