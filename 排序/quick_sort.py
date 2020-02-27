"""
快速排序
时间复杂度: 平均O(nlogn)，最坏O(n*n)
"""

def quick_sort(array):
    low = 0
    length = len(array)
    sort(array, low, length-1)

def sort(array, low, high):
    if low < high:
        pivot = pivot_partition(array, low, high)
        sort(array, low, pivot-1)
        sort(array, pivot+1, high)

def pivot_partition(array, low, high):
    pivot_value = array[low]

    while low < high:
        while (low < high) and (array[high] >= pivot_value):
            high -= 1
        array[low] = array[high]
        while (low < high) and (array[low] <= pivot_value):
            low += 1
        array[high] = array[low]

    array[low] = pivot_value
    return low


array= [5, 3, 6, 2, 10, 1, 4, 7, 9, 8]
quick_sort(array)
print(array)
