"""
题目：把一个数组最开始的若干个元素搬到数组的末尾，我们称之为数组的旋转。输入一个递增排序的数组
的一个旋转，输出旋转数组的最小元素。例如，数组{3, 4, 5, 1, 2}为{1, 2, 3, 4, 5}的一个旋
转，该数组的最小值为 1。
"""

def find_min(list):
    if (list is None) or (len(list) <= 0):
        return  None

    low = 0
    high = len(list) - 1
    mid = 0   # 若数组中的第一个数字最小，直接返回

    while (low < high) and (list[low] >= list[high]):

        if high - low == 1:
            mid = high
            break

        mid = (low + high) // 2

        # 如果low, mid, high指向的📚相等，则只能顺序查找
        if list[low] == list[mid] == list[high]:
            return find_min_order(list, low, high)

        if list[mid] >= list[low]:
            low = mid
        elif list[mid] <= list[high]:
            high = mid

    return list[mid]


def find_min_order(list, low, high):
    min = list[low]

    for i in range(low+1, high+1):
        if list[i] < min:
            min = list[i]

    return min



test_case1 = [3, 4, 5, 1, 2]
test_case2 = [1, 2, 3, 4, 5]
test_case3 = [1, 2, 3, 4, 5, 0, 1, 1]
test_case4 = [1, 0, 1, 1, 1]
test_case5 = [1, 1, 1, 0, 1]
test_case6 = [2, 2, 2, 2, 2]
test_case7 = [3]
test_case8 = []
test_case9 = None

print(find_min(test_case1))
print(find_min(test_case2))
print(find_min(test_case3))
print(find_min(test_case4))
print(find_min(test_case5))
print(find_min(test_case6))
print(find_min(test_case7))
print(find_min(test_case8))
print(find_min(test_case9))
