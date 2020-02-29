"""
题目：请实现一个函数，用来判断一棵二叉树是不是对称的。
如果一棵二叉树和它的镜像一样，那么它是对称的。
"""
class BinaryTreeNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def is_symmetrical(root):
    return is_symmetrical(root, root)

def is_symmetrical(root1, root2):
    if (root1 is None) and (root2 is None):
        return True

    if (root1 is None) or (root2 is None):
        return False

    if root1.value != root2.value:
        return False

    return is_symmetrical(root1.left, root2.right) \
           and is_symmetrical(root1.right, root2.left)
