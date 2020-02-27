"""
题目：给定一课二叉树和其中的一个节点，如何找出中序遍历序列的下一个节点？
树中的节点除了有两个分别指向左、右节点的指针，还有一个指向父节点的指针。
"""

class BinaryTreeNode():
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.parent = None


def get_next(node):

    if node is None:
        return None

    next = None

    if node.right is not None:
        right = node.right
        while right.left is not None:
            right = right.left

        next = right
    elif node.parent is not None:
        parent = node.parent
        current = node
        while (parent is not None) and (parent.right == current):
            current = parent
            parent = parent.parent
        next = parent

    return next
