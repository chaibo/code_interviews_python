"""
插入排序：将一个记录插入到已经排好序的有序表中，从而得到一个新的、记录数增 1 的有序表。
时间复杂度：最好O(n)，最坏O(n*n)，平均O(n*n)。
"""


def insertion_sort(array):
    if not array:
        return

    length = len(array)

    for i in range(1, length):
        if array[i] < array[i - 1]:
            temp = array[i]

            j = i - 1
            while (j >= 0) and array[j] > temp:
                array[j + 1] = array[j]
                j -= 1

            array[j + 1] = temp


if __name__ == '__main__':
    arr0 = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    insertion_sort(arr0)
    print(arr0)

    arr1 = [9, 1, 5, 8, 3, 7, 4, 6, 2, 0]
    insertion_sort(arr1)
    print(arr1)

    arr2 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    insertion_sort(arr2)
    print(arr2)
