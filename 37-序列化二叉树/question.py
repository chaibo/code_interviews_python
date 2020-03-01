"""
题目：请实现两个函数，分别用来序列化和反序列化二叉树。
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def ser(root):
    """
    利用前序遍历序列化二叉树。
    """
    if root is None:
        return ['$']

    result = [root.value]

    result.extend(ser(root.left))
    result.extend(ser(root.right))

    return result


def des(ser_list):
    if ser_list is None:
        return None

    list_iter = iter(ser_list)
    root = des_core(list_iter)
    return root


def des_core(ser_iter):
    value = next(ser_iter, None)
    if (value is None) or (value == '$'):
        return None

    root = BinaryTreeNode(value)
    root.left = des_core(ser_iter)
    root.right = des_core(ser_iter)

    return root
