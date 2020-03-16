"""
堆排序：将待排序的序列构造成一个大顶堆。此时，整个序列的最大值就是堆顶的根结点。将它移走（其实
就是将其与堆数组的末尾元素交换，此时末尾元素就是最大值），然后将剩余的 n-1 个序列重新构造成一
个堆，这样就会得到 n 个元素中的较大值。如此反复执行，便能得到一个有序序列。
"""


def heap_sort(array):
    if not array:
        return

    length = len(array)
    # 数组有效数字从索引 1 开始
    for i in range(length // 2, 0, -1):
        # 构建大顶堆
        build_heap(array, i, length - 1)

    last = length - 1
    while last > 1:
        swap(array, 1, last)
        last -= 1
        build_heap(array, 1, last)


def build_heap(array, i, length):
    while 2 * i <= length:
        j = 2 * i
        if (j < length) and (array[j] < array[j + 1]):
            j += 1

        if array[i] >= array[j]:
            break

        swap(array, i, j)
        i = j


def swap(array, i, j):
    temp = array[i]
    array[i] = array[j]
    array[j] = temp


if __name__ == '__main__':

    # 有效数字从索引 1 开始。
    arr0 = [-4, 3, 5, 6, 2, 4, 1, 0, 8, 7, 3, 9]
    heap_sort(arr0)
    print(arr0)

    arr1 = [-4, 9, 1, 5, 8, 3, 7, 4, 6, 2, 1, 0]
    heap_sort(arr1)
    print(arr1)

    arr2 = [-4, 1, 0, 2, 3, 4, 5, 6, 7, 0, 8, 9]
    heap_sort(arr2)
    print(arr2)
