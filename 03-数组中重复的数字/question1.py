"""
题目：找出数组中重复的数字
在一个长度为 n 的数组里所有数字都在 0~n-1 的范围内。数组中某些数字是重复的，但不知道
有几个数字重复，也不知道每个数字重复了几次。请找出数组中任意一个重复数字。例如，如果输
入长度为 7 的数组{2, 3, 1, 0, 2, 5, 3}，那么对应的输出是重复的数字 2 或者 3 。
"""

"""
时间复制度：O(n)
空间复杂度：O(1)
"""
def find_duplicate_number(array, length):

    if (array is None) or (length <= 0):
        return -1

    for num in array:
        if (num < 0) or (num >= length):
            return -1

    for i in range(length):
        while array[i] != i:
            num = array[i]
            if num == array[num]:
                return num
            else:
                array[i] = array[num]
                array[num] = num

    return -1

test_case1 = [2, 3, 1, 0, 2, 5, 3]
test_case2 = [0, 1, 2, 3, 4]
test_case3 = None
test_case4 = []
test_case5 = [0, 1, 3, 5]

print(find_duplicate_number(test_case1, 7))
print(find_duplicate_number(test_case2, 5))
print(find_duplicate_number(test_case3, 0))
print(find_duplicate_number(test_case4, 0))
print(find_duplicate_number(test_case5, 4))
