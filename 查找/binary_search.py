"""
二分查找
时间复杂度: O(logN)
"""

def binary_search(list, item):
    if list is None:
        return None

    low = 0
    high = len(list) - 1

    while low <= high:
        mid = (low + high) // 2    #向下取整
        num = list[mid]

        if num == item:
            return mid
        elif num > item:
            high = mid - 1
        else:
            low = mid + 1

    return None

test_list = [1, 3, 5, 6]

print(binary_search(test_list, 5))
print(binary_search(test_list, -1))

