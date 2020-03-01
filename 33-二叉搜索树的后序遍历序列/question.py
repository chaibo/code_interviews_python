"""
题目：输入一个整数数组，判断该数组是不是某二叉搜索树的后序遍历结果。
如果是则返回 True, 否则返回False。假设输入的数组的任意两个数字都不相同。
例如，输入数组 {5, 7, 6, 9, 11, 10, 8}，则返回 True。
如果输入的数组是 {7, 4, 6, 5}, 则由于没有哪棵二叉搜索树的后序遍历结果是
这个序列，因此返回 False。
"""


def verify_seq_of_bst(sequence):
    if (sequence is None) or (len(sequence) <= 0):
        return False

    length = len(sequence)
    root = sequence[length - 1]

    # 在二叉搜索树中左子树节点的值都小于根节点的值
    i = 0
    while i < length - 1:
        if sequence[i] > root:
            break
        i += 1

    # 在二叉搜索树中右子树节点的值都大于根节点的值
    j = i
    while j < length - 1:
        if sequence[j] < root:
            return False
        j += 1

    # 判断左子树是不是二叉搜索树
    left = True
    if i > 0:
        left = verify_seq_of_bst(sequence[: i])

    # 判断右子树是不是二叉搜索树
    right = True
    if i < length - 1:
        right = verify_seq_of_bst(sequence[i: length - 1])

    return left and right


def test():
    test_seq1 = [5, 7, 6, 9, 11, 10, 8]
    test_seq2 = [5, 6, 7, 8, 9]
    test_seq3 = [6, 5, 4, 3, 2, 1]
    test_seq4 = []
    test_seq5 = None
    test_seq6 = [1]
    test_seq7 = [7, 4, 6, 5]

    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq1, verify_seq_of_bst(test_seq1)))
    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq2, verify_seq_of_bst(test_seq2)))
    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq3, verify_seq_of_bst(test_seq3)))
    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq4, verify_seq_of_bst(test_seq4)))
    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq5, verify_seq_of_bst(test_seq5)))
    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq6, verify_seq_of_bst(test_seq6)))
    print("序列 {} 是否是二叉搜索树的后序遍历结果: {}"
          .format(test_seq7, verify_seq_of_bst(test_seq7)))


if __name__ == '__main__':
    test()
