"""
题目：给定一棵二叉搜索树，请找出其中第 k 大的节点。
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def kth_node(root, k):
    if (not root) or (k <= 0):
        return None

    result = None

    if root.left:
        result, k = kth_node(root.left, k)

    if not result:
        if k == 1:
            result = root
        k -= 1

    if (not result) and root.right:
        result, k = kth_node(root.right, k)

    return result, k
