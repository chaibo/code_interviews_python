"""
题目：数组中数值和下标相等的元素。
假设一个单调递增的数组里的每个元素都是整数并且是唯一的。请编程实现一个函数，找出数组
中任意一个数值等于其下标的元素。例如，在数组 {-3, -1, 1, 3, 5} 中，数字 3 和它的
下标相等。
"""


def get_num_same_as_index(array):
    if not array:
        return -1

    left = 0
    right = len(array) - 1

    while left <= right:
        mid = (left + right) // 2

        if array[mid] == mid:
            return mid
        elif array[mid] > mid:
            right = mid - 1
        else:
            left = mid + 1

    return -1


def test():
    array1 = None
    array2 = []
    array3 = [0]
    array4 = [1]
    array5 = [-3, -1, 1, 3, 5]
    array6 = [0, 2, 4, 5, 6]
    array7 = [-11, -8, -5, 0, 1, 5]
    array8 = [-3, -2, -1, 0, 1, 2]

    print("数组 {} 中数值和下标相等的元素是 {}.".format(array1,
                                          get_num_same_as_index(array1)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array2,
                                          get_num_same_as_index(array2)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array3,
                                          get_num_same_as_index(array3)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array4,
                                          get_num_same_as_index(array4)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array5,
                                          get_num_same_as_index(array5)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array6,
                                          get_num_same_as_index(array6)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array7,
                                          get_num_same_as_index(array7)))
    print("数组 {} 中数值和下标相等的元素是 {}.".format(array8,
                                          get_num_same_as_index(array8)))


if __name__ == '__main__':
    test()
