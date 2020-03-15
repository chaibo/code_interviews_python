"""
归并排序：要将一个数组排序，可以先（递归地）将它分成两半分别排序，然后将结果归并起来。
"""


def merge_sort0(array):
    """
    自顶向下。
    归并排序的递归实现。
    """
    if not array:
        return

    length = len(array)
    aux = [0] * length
    for i in range(length):
        aux[i] = array[i]

    merge_sort0_core(array, aux, 0, length - 1)


def merge_sort0_core(array, aux, low, high):
    if high <= low:
        return

    mid = (low + high) // 2
    merge_sort0_core(aux, array, low, mid)
    merge_sort0_core(aux, array, mid + 1, high)

    merge(array, aux, low, mid, high)


def merge_sort1(array):
    """
    自底向上。
    归并排序的循环实现。
    """

    if not array:
        return

    length = len(array)
    aux = [0] * length
    for i in range(length):
        aux[i] = array[i]

    temp = [array, aux]
    flag = 0

    size = 1  # 子数组的大小

    while size < length:
        low = 0
        while low < length - size:
            merge(temp[flag], temp[1 - flag], low, low + size - 1,
                  min(low + 2 * size - 1, length - 1))
            low = low + 2 * size

        flag = 1 - flag

        size *= 2

    if flag == 0:
        for i in range(length):
            array[i] = aux[i]


def merge(array, aux, low, mid, high):
    i, j = low, mid + 1

    for k in range(low, high + 1):
        if i > mid:
            array[k] = aux[j]
            j += 1
        elif j > high:
            array[k] = aux[i]
            i += 1
        elif aux[i] > aux[j]:
            array[k] = aux[j]
            j += 1
        else:
            array[k] = aux[i]
            i += 1


if __name__ == '__main__':
    arr0 = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    merge_sort1(arr0)
    print(arr0)
    arr0 = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    merge_sort0(arr0)
    print(arr0)

    arr1 = [9, 1, 5, 8, 3, 7, 4, 6, 2, 0]
    merge_sort1(arr1)
    print(arr1)
    arr1 = [9, 1, 5, 8, 3, 7, 4, 6, 2, 0]
    merge_sort0(arr1)
    print(arr1)

    arr2 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sort1(arr2)
    print(arr2)
    arr2 = [1, 0, 2, 3, 4, 5, 6, 7, 8, 9]
    merge_sort0(arr2)
    print(arr2)
