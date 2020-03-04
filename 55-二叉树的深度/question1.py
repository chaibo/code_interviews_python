"""
题目：二叉树的深度。
输入一棵二叉树的根节点，求该树的深度。从根节点到叶节点依次经过的节点(含根、叶节点) 形成
树的一条路径，最长路径的长度为树的深度。
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def tree_depth(root):
    if not root:
        return 0

    left = tree_depth(root.left)
    right = tree_depth(root.right)

    return max(left, right) + 1
