"""
二分查找
时间复杂度: O(logN)
"""


def binary_search(array, item):
    if array is None:
        return None

    low = 0
    high = len(array) - 1

    while low <= high:
        mid = (low + high) // 2  # 向下取整
        num = array[mid]

        if num == item:
            return mid
        elif num > item:
            high = mid - 1
        else:
            low = mid + 1

    return None


if __name__ == "__main__":
    l1 = [1, 3, 5, 6, 7, 8]
    print(binary_search(l1, 0))
    print(binary_search(l1, 3))
    print(binary_search(l1, 4))
    print(binary_search(l1, 9))
    print(binary_search([], 0))
    print(binary_search(None, 0))
