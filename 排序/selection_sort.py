"""
选择排序：首先，找到数组中最小的那个元素，其次，将它和数组的第一个元素交换位置（如果第一个元素就是
最小元素，那么它就和自己交换）。再次，在剩下的元素中找到最小的元素，将它与数组的第二个元素交换位置。
如此往复，直到将整个数组排序。
时间复杂度: O(n*n)
"""


def selection_sort(arr):
    if not arr:
        return

    length = len(arr)

    for i in range(length):
        min_index = i
        for j in range(i + 1, length):
            if arr[j] < arr[min_index]:
                min_index = j

        temp = arr[i]
        arr[i] = arr[min_index]
        arr[min_index] = temp


if __name__ == '__main__':
    arr = [3, 5, 6, 2, 4, 1, 0, 8, 7, 9]
    selection_sort(arr)
    print(arr)
