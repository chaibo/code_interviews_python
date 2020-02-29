"""
题目：输入两棵二叉树 A 和 B，判断 B 是不是 A 的子结构。
"""

class BinaryTreeNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def equal(num1, num2):
    """
    判断两个浮点数是否相等。
    """
    return abs(num1 - num2) < 0.0000001

def has_sub_tree(root1, root2):
    result = False

    if (root1 is not None) and (root2 is not None):
        if equal(root1.value, root2.value):
            result = has_sub_tree_core(root1, root2)
        if not result:
            result = has_sub_tree(root1.left, root2)
        if not result:
            result = has_sub_tree(root1.right, root2)

    return result

def has_sub_tree_core(root1, root2):
    if root2 is None:
        return True

    if root1 is None:
        return False

    if not equal(root1.value, root2.value):
        return False

    return has_sub_tree_core(root1.left, root2.left) \
           and has_sub_tree_core(root1.right, root2.right)
