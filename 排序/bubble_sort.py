"""
冒泡排序：两两比较相邻记录的关键字，如果反序列则交换，直到没有反序的记录为止。
时间复杂度：O(n*n)
"""


def bubble_sort0(array):
    """
    非标准冒泡排序，效率低。
    """
    if not array:
        return

    length = len(array)

    for i in range(length):
        for j in range(i + 1, length):
            if array[i] > array[j]:
                swap(array, i, j)


def bubble_sort1(array):
    """
    标准冒泡排序。
    """
    if not array:
        return

    length = len(array)

    for i in range(length):
        for j in range(length - 1, i, -1):
            if array[j - 1] > array[j]:
                swap(array, j - 1, j)


def bubble_sort2(array):
    """
    优化的冒泡排序。
    增加标记flag, 表示本轮比较是否有数据交换，如没有，则表示已经有序。
    """
    if not array:
        return

    length = len(array)

    flag = True
    for i in range(length):
        if not flag:
            break
        flag = False

        for j in range(length - 1, i, -1):
            if array[j - 1] > array[j]:
                swap(array, j - 1, j)
                flag = True


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == '__main__':
    arr0 = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    bubble_sort0(arr0)
    print(arr0)

    arr1 = [9, 1, 5, 8, 3, 7, 4, 6, 2, 0]
    bubble_sort1(arr1)
    print(arr1)

    arr2 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    bubble_sort0(arr2)
    print(arr2)
