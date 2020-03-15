"""
快速排序：通过一趟排序将待排记录分割成独立的两部分，其中一部分记录的关键字均比另一部分记录的关键
字小，则可分别对这两部分记录继续进行排序，以达到整个序列有序的目的。
时间复杂度: 平均O(nlogn)，最坏O(n*n)
"""


def quick_sort(array):
    low = 0
    length = len(array)
    sort(array, low, length - 1)


def sort(array, low, high):
    if low < high:
        pivot = pivot_partition(array, low, high)
        sort(array, low, pivot - 1)
        sort(array, pivot + 1, high)


def pivot_partition(array, low, high):
    pivot_value = array[low]

    while low < high:
        while (low < high) and (array[high] > pivot_value):
            high -= 1
        array[low] = array[high]
        while (low < high) and (array[low] <= pivot_value):
            low += 1
        array[high] = array[low]

    array[low] = pivot_value
    return low


if __name__ == '__main__':
    arr0 = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    quick_sort(arr0)
    print(arr0)

    arr1 = [9, 1, 5, 8, 3, 7, 4, 6, 2, 0]
    quick_sort(arr1)
    print(arr1)

    arr2 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    quick_sort(arr2)
    print(arr2)
