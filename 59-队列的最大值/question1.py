"""
题目：滑动窗口的最大值。
给定一个数组和滑动窗口的大小，请找出所有滑动窗口里的最大值。
例如，如果输入数组 {2, 3, 4, 2, 6, 2, 5, 1} 及滑动窗口的大小 3，那么
一共寸在 6 个滑动窗口，它们的最大值分别为 {4, 4, 6, 6, 6, 5}。
"""

from collections import deque


def max_in_windows(nums, size):
    max_in_win = []

    if nums and (1 <= size <= len(nums)):
        length = len(nums)
        idx = deque()

        for i in range(size):
            while idx and (nums[i] >= nums[idx[-1]]):
                idx.pop()

            idx.append(i)

        for i in range(size, length):
            max_in_win.append(nums[idx[0]])

            while idx and (nums[i] >= nums[idx[-1]]):
                idx.pop()
            if idx and (idx[0] <= i - size):
                idx.popleft()

            idx.append(i)

        max_in_win.append(nums[idx[0]])

    return max_in_win


def test():
    array1 = None
    array2 = []
    array3 = [2, 3, 4, 2, 6, 2, 5, 1]
    array4 = [1, 2, 3, 4, 5, 6, 7, 8]
    array5 = [8, 7, 6, 5, 4, 3, 2, 1]

    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array1, 2,
                                             max_in_windows(array1, 2)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array2, 2,
                                             max_in_windows(array2, 2)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array3, 3,
                                             max_in_windows(array3, 3)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array3, 0,
                                             max_in_windows(array3, 0)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array3, 1,
                                             max_in_windows(array3, 1)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array3, 8,
                                             max_in_windows(array3, 8)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array3, 9,
                                             max_in_windows(array3, 9)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array4, 3,
                                             max_in_windows(array4, 3)))
    print("数组: {}, 窗口大小: {}, 最大值: {}".format(array5, 3,
                                             max_in_windows(array5, 3)))


if __name__ == '__main__':
    test()
