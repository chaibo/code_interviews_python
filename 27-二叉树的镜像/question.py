"""
题目：请完成一个函数，输入一棵二叉树，该函数输出它的镜像。
"""

class BinaryTreeNode():

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def mirror_tree(tree_node):
    if tree_node is None:
        return

    if (tree_node.left is None) and (tree_node.right is None):
        return

    temp = tree_node.left
    tree_node.left = tree_node.right
    tree_node.right = temp

    if tree_node.left:
        mirror_tree(tree_node.left)

    if tree_node.right:
        mirror_tree(tree_node.right)
