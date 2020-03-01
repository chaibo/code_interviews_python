"""
题目：输入一棵二叉树和一个整数，打印出二叉树中节点值的和为输入整数的所有路径。
从树的根节点开始往下一直到叶节点所经过的节点形成一条路径。
"""


class BinaryTreeNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def find_path(root, sum):
    if root is None:
        return

    path = []
    current_sum = 0
    find_path(root, sum, path, current_sum)


def find_path(root, sum, path, current_sum):
    current_sum += root.value
    path.append(root.value)

    is_leaf = (root.left is None) and (root.right is None)

    if is_leaf and (sum == current_sum):
        print("有效路径：{}".format(path))

    if root.left is not None:
        find_path(root.left, sum, path, current_sum)
    if root.right is not None:
        find_path(root.right, sum, path, current_sum)

    # 在返回父节点之前，在路径上删除当前节点
    path.pop()
