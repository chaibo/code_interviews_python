"""
题目：不修改数组找出重复的数字
在一个长度为 n+1 的数组里的所有数字都在 1~n 的范围内，所以数组中至少有一个数字是重复
的。请找出数组中任意一个重复的数字，但不能修改输入的数组。例如，如果输入长度为 8 的数
组{2, 3, 5, 4, 3, 2, 6, 7}, 那么对应的输出是重复的数字 2 或者 3。
"""

"""
时间复制度：O(nlogn)
空间复杂度：O(1)
"""
def find_duplicate_number(array, length):
    if (array is None) or (length <= 0):
        return -1

    for num in array:
        if (num <= 0) or (num >= length):

            return -1

    start = 1
    end = length - 1
    while start <= end:
        middle = (start + end) // 2
        count = count_range(array, start, middle)
        if start == end:
            if count > 1:
                return start
            else:
                break

        if count > (middle - start + 1):
            end = middle
        else:
            start = middle + 1

    return -1


def count_range(array, start, end):
    if array is None:
        return 0
    count = 0
    for num in array:
        if start <= num <=end:
            count += 1

    return count


test_case1 = [2, 3, 5, 4, 3, 2, 6, 7]
test_case2 = [0, 2, 2, 2, 2, 5, 6, 7]
test_case3 = None
test_case4 = []
test_case5 = [1, 2, 3, 4]

print(find_duplicate_number(test_case1, 8))
print(find_duplicate_number(test_case2, 8))
print(find_duplicate_number(test_case3, 0))
print(find_duplicate_number(test_case4, 0))
print(find_duplicate_number(test_case5, 4))
