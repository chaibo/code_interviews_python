"""
希尔排序：交换不相邻的元素以对数组的局部进行排序，并最终用插入排序将局部有序的数组排序。
"""


def shell_sort(array):
    if not array:
        return

    length = len(array)
    increment = 1
    while increment < length // 3:
        increment = 3 * increment + 1

    while increment >= 1:

        for i in range(increment, length):
            if array[i] < array[i - increment]:
                temp = array[i]

                j = i - increment
                while (j >= 0) and array[j] > temp:
                    array[j + increment] = array[j]
                    j -= increment

                array[j + increment] = temp

        increment = increment // 3


if __name__ == '__main__':
    arr0 = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    shell_sort(arr0)
    print(arr0)

    arr1 = [9, 1, 5, 8, 3, 7, 4, 6, 2, 0]
    shell_sort(arr1)
    print(arr1)

    arr2 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    shell_sort(arr2)
    print(arr2)